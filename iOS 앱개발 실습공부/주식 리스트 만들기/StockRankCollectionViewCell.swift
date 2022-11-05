//
//  StockRankCollectionViewCell.swift
//  StockRank
//
//  Created by 최민기 on 2022/11/03.
//

import UIKit

class StockRankCollectionViewCell: UICollectionViewCell {
    
    //uicomponent 연결하자
    // uicomponent에 데이터를 업데이트 하는 코드를 넣자
    
    @IBOutlet weak var companyIconImageView: UIImageView!
    
    @IBOutlet weak var rankLable: UILabel!
    
    @IBOutlet weak var companyNameLabel: UILabel!
    
    @IBOutlet weak var companyPriceLabel: UILabel!
    
    @IBOutlet weak var diffLabel: UILabel!
    
    func configure(_ stock: StockModel) {
        rankLable.text = "\(stock.rank)"
        companyIconImageView.image = UIImage(named: stock.imageName)
        companyNameLabel.text = stock.name
        companyPriceLabel.text = "\(convertToCurrencyFormat(price:stock.price)) 원"
//        let color : UIColor
//        if stock.diff > 0 {
//            color = UIColor.systemRed
//        } else {
//            color = UIColor.systemBlue
//        }
//        diffLabel.textColor = color
        diffLabel.textColor = stock.diff > 0 ? UIColor.systemRed : UIColor.systemBlue
        diffLabel.text = "\(stock.diff)"
    }
    
    // 주식 금액에서 3자리 숫자마다 , 찍어주는 함수 생성하기 !
    
    func convertToCurrencyFormat(price : Int) -> String {
        let numberFormatter = NumberFormatter()
        numberFormatter.numberStyle = .decimal
        numberFormatter.maximumFractionDigits = 0
        let result = numberFormatter.string(from: NSNumber(value: price)) ?? ""  // 옵셔널 언래핑을 통해 result 값이 return 되도록 한다.   ?? "" < 를 할 경우 강제 언래핑이 아닌 값이 없는 경우 빈값으로 출력해 달라는 문구를 통해 에러를 방지할 수 있다. -> 강제 언래핑보다 더 효율적이다. 많이 쓰기도 한다.
        return result
    }
    
    
    // 과제 : 주식 값이 상승했을 때 빨간색으로 , 하락했을 때 파란색으로 표현하기 !
    
    // 강사팀 풀이
//    let color : UIColor
//    if stock.diff > 0 {
//        color = UIColor.systemRed
//    } else {
//        color = UIColor.systemBlue
//    }
//    diffLabel.textColor = color
//    diffLabel.text = "\(stock.diff)"
    
    // 삼항 연산자 사용법 !
    // diffLabel.textColor = 조건 ? true 일때 : false 일때
    
    
}
