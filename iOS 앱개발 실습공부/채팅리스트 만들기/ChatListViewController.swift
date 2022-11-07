//
//  ChatListViewController.swift
//  ChatList
//
//  Created by 최민기 on 2022/11/05.
//

import UIKit

class ChatListViewController: UIViewController {
    
    // 컬렉션 뷰 삽입
    @IBOutlet weak var collectionView: UICollectionView!
    
    var chatList : [Chat] = Chat.list
    
    override func viewDidLoad() {
        super.viewDidLoad()
        
        // 컬렉션 뷰를 데이터를 표현하기 위해 필요한 3가지
        // Data, Presentation, Layout
        
        // 정보 전달 - 담당자 : viewController
        collectionView.dataSource = self
        // 레이아웃 담당자 = viewcontroller
        collectionView.delegate = self
        
        // 날짜 순으로 최신부터 보여주게 정렬  // 선택 정렬
        chatList = chatList.sorted(by: { chat1, chat2 in
            return chat1.date > chat2.date
        })
        
        
    }
}

// 규칙 준수를 위해 먼저 함수 구현
// 정보 전달 담당자 위임
extension ChatListViewController : UICollectionViewDataSource {
    func collectionView(_ collectionView: UICollectionView, numberOfItemsInSection section : Int) -> Int {
        return chatList.count
    }
    
    
    // 레이아웃 맞추기
    func collectionView(_ collectionView: UICollectionView, cellForItemAt indexPath: IndexPath) -> UICollectionViewCell {
        guard let cell = collectionView.dequeueReusableCell(withReuseIdentifier: "ChatListCollectionViewCell", for: indexPath) as? ChatListCollectionViewCell else {
            return UICollectionViewCell()
        }
                
        let chat = chatList[indexPath.item]
        // 만들어진 채팅방에 데이터 삽입하기
        cell.configure(chat)
        // 데이터를 삽입한 cell값 반환 .
        return  cell
    }
}

// 레이아웃 역할 위임
extension ChatListViewController: UICollectionViewDelegateFlowLayout {
    func collectionView(_ collectionView: UICollectionView, layout collectionViewLayout: UICollectionViewLayout, sizeForItemAt indexPath: IndexPath) -> CGSize {
        return CGSize(width: collectionView.bounds.width, height: 100)
    }
}
