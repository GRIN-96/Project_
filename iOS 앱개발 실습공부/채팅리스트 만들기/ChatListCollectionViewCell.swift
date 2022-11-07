//
//  ChatListCollectionViewCell.swift
//  ChatList
//
//  Created by 최민기 on 2022/11/05.
//

import UIKit

class ChatListCollectionViewCell: UICollectionViewCell {
    
    // 채팅 리스트에 보이는 프로필 사진
    @IBOutlet weak var thumbnail: UIImageView!
    // 상대방 이름
    @IBOutlet weak var nameLable: UILabel!
    // 마지막 채팅 내용
    @IBOutlet weak var chatLable: UILabel!
    // 마지막 채팅을 보낸 날짜
    @IBOutlet weak var dateLable: UILabel!
    
    
    override func awakeFromNib() {
        // 스토리 보드에서 꺼내올 때 호출되는 함수
        super.awakeFromNib()
        
        // 프로필 사진 이미지를 모서리를 둥글게 만들어주는 코드.
        thumbnail.layer.cornerRadius = 10
    }
    
    
    func configure(_ chat: Chat) {
        thumbnail.image = UIImage(named: chat.name)
        nameLable.text = chat.name
        chatLable.text = chat.chat
        dateLable.text = formattedDateString(dateString: chat.date)
    }
    
    func formattedDateString(dateString : String) -> String {
        // String -> Date -> String
        //2022-04-01 > 4/1
        
        let formatter = DateFormatter()
        formatter.dateFormat = "yyyy-MM-dd"
        
        //문자열을 date type로 변경하는 법
        if let date = formatter.date(from: dateString) {
            formatter.dateFormat = "M/d"
            return formatter.string(from:date)
        }else {
            return ""
        }
    }
    
}
