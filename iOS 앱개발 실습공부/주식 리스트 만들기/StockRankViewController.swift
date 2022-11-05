//
//  StockRankViewController.swift
//  StockRank
//
//  Created by 최민기 on 2022/11/03.
//

import UIKit


class StockRankViewController: UIViewController {
    
    @IBOutlet weak var collectionView: UICollectionView!
    
    
    let stockList : [StockModel] = StockModel.list

    
    
    // DATA, Presentation, Layout
    // Data - 어떤 데이터?  -> StockList
    // Presentation - 셀을 어떻게 표현 ?
    // Layout = 셀을 어떻게 배치할거야 ?
    
    
    // protocol -
    
    override func viewDidLoad() {
        super.viewDidLoad()
        
        collectionView.dataSource = self
        collectionView.delegate = self
    

    }

}

extension StockRankViewController: UICollectionViewDataSource {
    func collectionView(_ collectionView: UICollectionView, numberOfItemsInSection section: Int) -> Int {
        return stockList.count
    }
    
    func collectionView(_ collectionView: UICollectionView, cellForItemAt indexPath: IndexPath) -> UICollectionViewCell {
        // 데이터 업데이트
        
    /**
       // guard <dddd 꼭 참이어야 하는 조건> else {
//        return ....xxx
    //    }
    //    xx xxxx
     
      */
        
        guard let cell = collectionView.dequeueReusableCell(withReuseIdentifier: "StockRankCollectionViewCell", for: indexPath) as? StockRankCollectionViewCell else {
            return UICollectionViewCell()
        }
        let stock = stockList[indexPath.item]
        cell.configure(stock)
        return cell
        }
        
       
    }

extension StockRankViewController: UICollectionViewDelegateFlowLayout {
    // 레이아웃 지정하는 컨트롤러
    func collectionView(_ collectionView: UICollectionView, layout collectionViewLayout: UICollectionViewLayout, sizeForItemAt indexPath : IndexPath) -> CGSize {
        // width == collectionView
        // 80
        return CGSize(width: collectionView.bounds.width, height:80)
    }
}

