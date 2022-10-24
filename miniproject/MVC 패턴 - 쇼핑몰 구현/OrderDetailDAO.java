package dao;

import java.sql.Connection;
import java.sql.PreparedStatement;
import java.sql.ResultSet;
import java.sql.SQLException;
import java.util.ArrayList;

import b2c_dto.OrderDetailDTO;
import dbutil.DBUtil;

public class OrderDetailDAO {
//DAO : DB와 연동해 데이터를 입력, 수정, 삭제 등을 수행하는 클래스. 여기서 본격적인 SQL 쿼리가 수행됨.
	// Insert, Update, Delete methods ...
	
	//1. 유저의 장바구니를 주문으로 넣어주는 경우.
	  public static boolean insertOrderDetail(String id) throws SQLException {

	    Connection con = null; // Connection :: DB와 JAVA를 연결시켜주는 역할을 하는 객체이다.
	    PreparedStatement pstmt = null; // PreparedStatement :: SQL문을 실행할 때 실행을 위한 SQL을 DB에 전달하는 역할을 수행하는 객체다.
	     System.out.println("작업중입니다.");
	     
	    //order_id, prodnum, pname, price, quantity
	    try {

	      //1. DB 연결
	      con = DBUtil.getConnection();
	      pstmt = con.prepareStatement("insert into order_detail(order_id, prodnum, pname, price, quantity) select order_id, prodnum, pname, price, quantity from cart where order_id = (?)"); // '?'는 아직 값이 정해지지 않은 SQL문의 변수를 의미한다.
	      //2. SQL Query 완성
	        // .setString()을 사용하여 각각의 ?위치에 값을 String으로 입력한다. (index, value)순서
	      pstmt.setString(1, id);
	      
	      
	      //3. Query 실행
	      int result = pstmt.executeUpdate(); //.executeUpdate() :: Compile된 DML문을 실행시킴. 성공적으로 수행된 경우 1, 실패한 경우 0 을 반환한다.
	      if (result == 1) {
	    	  System.out.println("작업이 완료되었습니다.");
	        return true;
	      } 
	    } finally {
	      DBUtil.close(con, pstmt); //DB connection 종료
	    } return false;
	  }
	  
	  
	  
	  
	  //2. 주문번호 달아주기
	  
	  public static boolean updateOrderDetail(String id) throws SQLException {

		    Connection con = null; // Connection :: DB와 JAVA를 연결시켜주는 역할을 하는 객체이다.
		    PreparedStatement pstmt = null; // PreparedStatement :: SQL문을 실행할 때 실행을 위한 SQL을 DB에 전달하는 역할을 수행하는 객체다.
		     System.out.println("주문번호 작업중입니다.");
		     
		    //order_id, prodnum, pname, price, quantity
		    try {

		      //1. DB 연결
		      con = DBUtil.getConnection();
		      pstmt = con.prepareStatement("UPDATE order_detail SET order_infomation = (select ordernum from orders where order_id = ? order by order_id =? desc limit 1) WHERE order_id = ? and order_infomation is null"); // '?'는 아직 값이 정해지지 않은 SQL문의 변수를 의미한다.
		      //2. SQL Query 완성
		        // .setString()을 사용하여 각각의 ?위치에 값을 String으로 입력한다. (index, value)순서
		      pstmt.setString(1, id);
		      pstmt.setString(2, id);
		      pstmt.setString(3, id);
		      
		      
		      //3. Query 실행
		      int result = pstmt.executeUpdate(); //.executeUpdate() :: Compile된 DML문을 실행시킴. 성공적으로 수행된 경우 1, 실패한 경우 0 을 반환한다.
		      if (result == 1) {
		    	  System.out.println("작업이 완료되었습니다.");
		        return true;
		      } 
		    } finally {
		      DBUtil.close(con, pstmt); //DB connection 종료
		    } return false;
		  }
	  
	  
	// 3. 주문 상세내역 호출
	  public static ArrayList<OrderDetailDTO> searchOrderDetailnum(int ordernum) throws SQLException {
			Connection con = null;
			PreparedStatement pstmt = null;
			ResultSet rs = null;  //ResultSet :: select 문을 실행했을 경우 데이터베이스에서 결과를 받아와 저장하는 객체이다.
			ArrayList<OrderDetailDTO> list = new ArrayList<OrderDetailDTO>(); //반환할 모든 Seller객체 정보를 담을 ArrayList 생성
			try {
			  con = DBUtil.getConnection();
			  pstmt = con.prepareStatement("SELECT * FROM order_detail WHERE order_infomation =?");
			  pstmt.setInt(1, ordernum);
			  
			  rs = pstmt.executeQuery();
			  while (rs.next()) { // .next() : 수행결과로 ResultSet객체에서 하나의 Row를 반환한다. 더이상 결과가 없을 경우 false를 반환하면서 리턴
			                      // next()메소드를 한번 호출할때마다 한개의 레코드를 아이템으로 가진 객체를 반환한다.
			
				  OrderDetailDTO user = new OrderDetailDTO(
		    		rs.getInt("ordernum"), 
		    		rs.getString("order_id"), 
		    		rs.getInt("prodnum"), 
		    		rs.getString("pname"), 
		            rs.getInt("price"),
		            rs.getInt("quantity"),
		            rs.getInt("order_infomation")
		        );
			    list.add(user); //각 User객체를 ArrayList에 추가
			  }
			} finally {
			  DBUtil.close(con, pstmt, rs);
			} return list;
			}
	  
	  
	  // 4. 총합 구해주기
	  public static int sumOrderDetail(int ordernum) throws SQLException {
		    Connection con = null;
		    PreparedStatement pstmt = null;
		    ResultSet rs = null;
		    int list = 0;
		    System.out.println("계산중입니다.");
		    try {
		      con = DBUtil.getConnection();
		      pstmt = con.prepareStatement("select sum(quantity * price) from order_detail where order_infomation = ? ");
		      pstmt.setInt(1, ordernum);
		      
		      rs = pstmt.executeQuery();
		      while (rs.next()){
		    	  list = rs.getInt("sum(quantity * price)");

		      }
		    } finally {
		      DBUtil.close(con, pstmt, rs);
		    } 
			return list;
		  }
			

		
}
