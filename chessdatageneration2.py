import os
import numpy as np
import pandas as pd
import csv

data = pd.read_csv('chessData.csv')#change with CSV path

board = []
for idx, row in data.iterrows():
  wp = []
  bp = []
  wk = []
  bk = []
  wq = []
  bq = []
  wb = []
  bb = []
  wn = []
  bn = []
  wr = []
  br = []
  turn = 2
  WKingside = 0
  WQueenside = 0
  BKingside = 0
  BQueenside = 0
  currentrow = 7
  currentcol = 0
  end = False
  for c in row['FEN']:
    if(c == ' '):
      end = True
    if not end:
      if(c == '/'):
        currentrow -=1
        currentcol = 0
        continue
      if(c.isdigit()):
        currentcol+=int(c)
        continue
      if c == 'p':
        bp.append(currentrow * 8 + currentcol)
      elif c == 'P':
        wp.append(currentrow * 8 + currentcol)
      elif c == 'b':
        bb.append(currentrow * 8 + currentcol)
      elif c == 'B':
        wb.append(currentrow * 8 + currentcol)
      elif c == 'n':
        bn.append(currentrow * 8 + currentcol)
      elif c == 'N':
        wn.append(currentrow * 8 + currentcol)
      elif c == 'r':
        br.append(currentrow * 8 + currentcol)
      elif c == 'R':
        wr.append(currentrow * 8 + currentcol)
      elif c == 'k':
        bk.append(currentrow * 8 + currentcol)
      elif c == 'K':
        wk.append(currentrow * 8 + currentcol)
      elif c == 'q':
        bq.append(currentrow * 8 + currentcol)
      elif c == 'Q':
        wq.append(currentrow * 8 + currentcol)
    currentcol+=1
    if end:
      if c == 'w':
        turn = 1
      elif c == 'b' and turn == 2:
        turn = 0
      if c == 'K':
        WKingside = 1
      elif c == 'Q':
        WQueenside = 1
      if c == 'k':
        BKingside = 1
      elif c == 'q':
        BQueenside = 1
  eval = row['Evaluation']
  if eval[0] == '+':
    eval = eval[1:]
  elif eval[0] == '#':
    eval = 10000
  eval = int(eval)
  board = [wp, wr, wn, wb, wk, wq, bp, br, bn, bb, bk, bq]
  with open(r'chessDataBetter.csv', 'a', newline='') as csvfile:#change CSV with desired CSV file path
    fieldnames = ['board', 'whitecastling', 'blackcastling', 'turn', 'eval']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writerow({'board': [wp, wr, wn, wb, wk, wq, bp, br, bn, bb, bk, bq],'whitecastling':[WKingside, WQueenside], 'blackcastling':[BKingside, BQueenside], 'turn':turn, 'eval': eval})
