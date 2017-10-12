{
 "cells": [
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "#### アサヒビールの購入意向の変化を表す変数作成したよ\n",
    "全部の変数にはまだ応用できてない！"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": [
    "import pandas as pd"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "collapsed": false
   },
   "outputs": [],
   "source": [
    "df = pd.read_csv(\"/Volumes/Sony_8GT/NRI_データ解析コンペ/アンケートデータ/CSV/メインデータ_2017.csv\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "collapsed": false
   },
   "outputs": [],
   "source": [
    "df.head()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "collapsed": false
   },
   "outputs": [],
   "source": [
    "#欠損値処理\n",
    "df = df[df[\"PI_01_752601\"]!=' ']\n",
    "df = df[df[\"PI_02_752601\"]!=' ']\n",
    "len(df)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "collapsed": false
   },
   "outputs": [],
   "source": [
    "#object型→int型\n",
    "int1_list = list(df[\"PI_01_752601\"].values.flatten())\n",
    "int1_list = [int(x) for x in int1_list]\n",
    "\n",
    "int2_list = list(df[\"PI_02_752601\"].values.flatten())\n",
    "int2_list = [int(x) for x in int2_list]\n",
    "\n",
    "df[\"PI_01_752601\"] = int1_list\n",
    "df[\"PI_02_752601\"] = int2_list"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "|  |1.ぜひ買いたい| 2.買いたい | 3.わからない |4.買いたくない|\n",
    "|:-----:|:----:|:-----:|:-----:|:----:|\n",
    "| **1.ぜひ買いたい** | 0| -1 |-2|-3|\n",
    "| **2.買いたい** | 1| 0 |-1|-2|\n",
    "| **3.わからない** | 2| 1 |0|-1|\n",
    "| **4.買いたくない** | 3| 2 |1|0|\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "collapsed": false
   },
   "outputs": [],
   "source": [
    "#態度変化\n",
    "df[\"trans_752601\"] = df[\"PI_01_752601\"]-df[\"PI_02_752601\"] "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "collapsed": false
   },
   "outputs": [],
   "source": [
    "df.groupby(\"trans_752601\").size()"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "基本的には意向は変化してないけどポジティブ（ネガティブ）な変化も一定数いるね."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.6.0"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
