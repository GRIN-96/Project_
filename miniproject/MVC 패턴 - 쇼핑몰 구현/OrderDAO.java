package dao;

import java.sql.Connection;
import java.sql.PreparedStatement;
import java.sql.ResultSet;
import java.sql.SQLException;
import java.time.LocalDate;
import java.util.ArrayList;

import b2c_dto.OrderDTO;
import b2c_dto.ProductDTO;
import b2c_dto.UserDTO;
import dbutil.DBUtil;

public class OrderDAO {
	//DAO : DB와 연동해 데이터를 입력, 수정, 삭제 등을 수행하는 클래스. 여기서 본격적인 SQL 쿼리가 수행됨.
		// Insert, Update, Delete methods ...
		
		//1. 새로운 주문을 DB에 추가하는 메소드
		  public static boolean addOrder(OrderDTO neworder) throws SQLException {

		    Connection con = null; // Connection :: DB와 JAVA를 연결시켜주는 역할을 하는 객체이다.
		    PreparedStatement pstmt = null; // PreparedStatement :: SQL문을 실행할 때 실행을 위한 SQL을 DB에 전달하는 역할을 수행하는 객체다.
		    //  order가 갖는 속성 : ordernum, order_id, total_price, indete, result
		    		
		    try {

		      //1. DB 연결
		      con = DBUtil.getConnection();
		      pstmt = con.prepareStatement("INSERT INTO orders (order_id, indate) VALUES(?, ?)"); // '?'는 아직 값이 정해지지 않은 SQL문의 변수를 의미한다.
		      LocalDate currentdate = LocalDate.now();
		      
		      pstmt.setString(1, neworder.getOrderId());
		      pstmt.setString(2, currentdate.toString());
		      
		      //3. Query 실행
		      int result = pstmt.executeUpdate(); //.executeUpdate() :: Compile된 DML문을 실행시킴. 성공적으로 수행된 경우 1, 실패한 경우 0 을 반환한다.
		      if (result == 1) {
		    	  System.out.println("주문이 완료 되었습니다.");
		        return true;
		      } 
		    } finally {
		      DBUtil.close(con, pstmt); //DB connection 종료
		    }
		    return false;
		  }
		  
		  
		  
	  //2. 주문 정보 호출
	  public static ArrayList<OrderDTO> searchOrder(String id) throws SQLException {
			Connection con = null;
			PreparedStatement pstmt = null;
			ResultSet rs = null;  //ResultSet :: select 문을 실행했을 경우 데이터베이스에서 결과를 받아와 저장하는 객체이다.
			ArrayList<OrderDTO> list = new ArrayList<OrderDTO>(); //반환할 모든 Seller객체 정보를 담을 ArrayList 생성
			try {
			  con = DBUtil.getConnection();
			  pstmt = con.prepareStatement("SELECT * FROM orders WHERE order_id =?");
			  pstmt.setString(1, id);
			  
			  rs = pstmt.executeQuery();
			  while (rs.next()) { // .next() : 수행결과로 ResultSet객체에서 하나의 Row를 반환한다. 더이상 결과가 없을 경우 false를 반환하면서 리턴
			                      // next()메소드를 한번 호출할때마다 한개의 레코드를 아이템으로 가진 객체를 반환한다.
			
				  OrderDTO user = new OrderDTO(
		    		rs.getInt("ordernum"), //ResultSet에서 getString()을 사용하여 각각의 컬럼의 값을 가져온다.
		            rs.getString("order_id"),
		            rs.getString("indate"),
		            rs.getString("result")
		        );
			    list.add(user); //각 User객체를 ArrayList에 추가
			  }
			} finally {
			  DBUtil.close(con, pstmt, rs);
			} return list;
			}
	  
	  // 2-1. 주문번호로 호출 
  public static ArrayList<OrderDTO> searchOrdernum(int ordernum) throws SQLException {
		Connection con = null;
		PreparedStatement pstmt = null;
		ResultSet rs = null;  //ResultSet :: select 문을 실행했을 경우 데이터베이스에서 결과를 받아와 저장하는 객체이다.
		ArrayList<OrderDTO> list = new ArrayList<OrderDTO>(); //반환할 모든 Seller객체 정보를 담을 ArrayList 생성
		try {
		  con = DBUtil.getConnection();
		  pstmt = con.prepareStatement("SELECT * FROM orders WHERE ordernum =?");
		  pstmt.setInt(1, ordernum);
		  
		  rs = pstmt.executeQuery();
		  while (rs.next()) { // .next() : 수행결과로 ResultSet객체에서 하나의 Row를 반환한다. 더이상 결과가 없을 경우 false를 반환하면서 리턴
		                      // next()메소드를 한번 호출할때마다 한개의 레코드를 아이템으로 가진 객체를 반환한다.
		
			  OrderDTO user = new OrderDTO(
	    		rs.getInt("ordernum"), //ResultSet에서 getString()을 사용하여 각각의 컬럼의 값을 가져온다.
	            rs.getString("order_id"),
	            rs.getString("indate"),
	            rs.getString("result")
	        );
		    list.add(user); //각 User객체를 ArrayList에 추가
		  }
		} finally {
		  DBUtil.close(con, pstmt, rs);
		} return list;
		}
  
  
  // 3. 배송 현황 변경.
  public static boolean updateOrder(int ordernum, String result1) throws SQLException {

	    Connection con = null; // Connection :: DB와 JAVA를 연결시켜주는 역할을 하는 객체이다.
	    PreparedStatement pstmt = null; // PreparedStatement :: SQL문을 실행할 때 실행을 위한 SQL을 DB에 전달하는 역할을 수행하는 객체다.
	    //  order가 갖는 속성 : ordernum, order_id, total_price, indete, result
	    		
	    try {

	      //1. DB 연결
	      con = DBUtil.getConnection();
	      pstmt = con.prepareStatement("update orders set result =? where ordernum = ?"); // '?'는 아직 값이 정해지지 않은 SQL문의 변수를 의미한다.
	      
	      pstmt.setString(1, result1);
	      pstmt.setInt(2, ordernum);
	      
	      //3. Query 실행
	      int result = pstmt.executeUpdate(); //.executeUpdate() :: Compile된 DML문을 실행시킴. 성공적으로 수행된 경우 1, 실패한 경우 0 을 반환한다.
	      if (result == 1) {
	    	  System.out.println("배송 현황이 변경되었습니다.");
	        return true;
	      } 
	    } finally {
	      DBUtil.close(con, pstmt); //DB connection 종료
	    }
	    return false;
	  }
  
  
  
		  
		  
		  
}
