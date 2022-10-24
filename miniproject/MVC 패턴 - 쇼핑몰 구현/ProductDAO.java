package dao;

import java.sql.Connection;
import java.sql.PreparedStatement;
import java.sql.ResultSet;
import java.sql.SQLException;
import java.time.LocalDate;
import java.util.ArrayList;

import b2c_dto.ProductDTO;
import b2c_dto.UserDTO;
import dbutil.DBUtil;

public class ProductDAO {
	//DAO : DB와 연동해 데이터를 입력, 수정, 삭제 등을 수행하는 클래스. 여기서 본격적인 SQL 쿼리가 수행됨.
	// Insert, Update, Delete methods ...
	
	//1. 새로운 Product를 DB에 추가하는 메소드
	  public static boolean insertProduct(ProductDTO product) throws SQLException {

	    Connection con = null; // Connection :: DB와 JAVA를 연결시켜주는 역할을 하는 객체이다.
	    PreparedStatement pstmt = null; // PreparedStatement :: SQL문을 실행할 때 실행을 위한 SQL을 DB에 전달하는 역할을 수행하는 객체다.
	      
	     
	    // product가 갖는 속성prodNum int, pname var, kind var, price int, content var, useyn var, regdate date
	    try {

	      //1. DB 연결
	      con = DBUtil.getConnection();
	      pstmt = con.prepareStatement("INSERT INTO product (seller_id, pname, kind, price, content, regdate) VALUES(?,?, ?, ?, ?, ?)"); // '?'는 아직 값이 정해지지 않은 SQL문의 변수를 의미한다.
	      LocalDate currentdate = LocalDate.now();

	      //2. SQL Query 완성
	        // .setString()을 사용하여 각각의 ?위치에 값을 String으로 입력한다. (index, value)순서
	      pstmt.setString(1, product.getSellerId());
	      pstmt.setString(2, product.getPname());
	      pstmt.setString(3, product.getKind());
	      pstmt.setInt(4, product.getPrice());
	      pstmt.setString(5, product.getContent());
	      pstmt.setString(6, currentdate.toString());   // 신엽님 최고 뇌섹남
	      
	      
	      //3. Query 실행
	      int result = pstmt.executeUpdate(); //.executeUpdate() :: Compile된 DML문을 실행시킴. 성공적으로 수행된 경우 1, 실패한 경우 0 을 반환한다.
	      if (result == 1) {
	    	  System.out.println("상품 등록이 완료되었습니다.");
	        return true;
	      } 
	    } finally {
	      DBUtil.close(con, pstmt); //DB connection 종료
	    } return false;
	  }
	  
	  
	  //2. 물품 금액 변경
	  public static boolean updateProductPrice(String id, int prodNum, Double newprice) throws SQLException {
			Connection con = null;
			PreparedStatement pstmt = null;
			System.out.println("이벤트로인한 10% 할인가 적용중입니다.");
			try {
		      con = DBUtil.getConnection(); // db 연결
		      	
				pstmt = con.prepareStatement("UPDATE product SET price = price*? WHERE seller_id=? AND prodNum=?");
				pstmt.setDouble(1, newprice);
				pstmt.setString(2, id);
				pstmt.setInt(3, prodNum);

				int result = pstmt.executeUpdate();
				if (result == 1) {
					System.out.println("금액 변경이 완료되었습니다.");
					return true;
				}else {
					System.out.println("정보가 잘못 입력되었습니다. 다시 시도해 주세요");
				}
			} finally {
				DBUtil.close(con, pstmt);
			}
			return false;
		}
	  
	  
	  // 3. 재고 현황 변경
	  public static boolean updateProductYN(String id, int prodNum, String useyn) throws SQLException {
			Connection con = null;
			PreparedStatement pstmt = null;
			System.out.println("재고 현황 데이터를 수정합니다.");
			try {
		      con = DBUtil.getConnection(); // db 연결
		      	
				pstmt = con.prepareStatement("UPDATE product SET useyn=? WHERE seller_id=? AND prodNum=?");
				pstmt.setString(1, useyn);
				pstmt.setString(2, id);
				pstmt.setInt(3, prodNum);

				int result = pstmt.executeUpdate();
				if (result == 1) {
					System.out.println("수정이 완료되었습니다.");
					return true;
				}
			} finally {
				DBUtil.close(con, pstmt);
			}
			return false;
		}
	  
	  
	  // 4. 모든 물품 조회
	  public static ArrayList<ProductDTO> getAllProduct() throws SQLException {
			Connection con = null;
			PreparedStatement pstmt = null;
			ResultSet rs = null;  //ResultSet :: select 문을 실행했을 경우 데이터베이스에서 결과를 받아와 저장하는 객체이다.
			ArrayList<ProductDTO> lists = new ArrayList<ProductDTO>(); //반환할 모든 Seller객체 정보를 담을 ArrayList 생성
			try {
			  con = DBUtil.getConnection();
			  pstmt = con.prepareStatement("SELECT * FROM product");
			  rs = pstmt.executeQuery();
			  while (rs.next()) { // .next() : 수행결과로 ResultSet객체에서 하나의 Row를 반환한다. 더이상 결과가 없을 경우 false를 반환하면서 리턴
			                      // next()메소드를 한번 호출할때마다 한개의 레코드를 아이템으로 가진 객체를 반환한다.
			
			    ProductDTO product = new ProductDTO(
		    		rs.getInt("prodNum"), //ResultSet에서 getString()을 사용하여 각각의 컬럼의 값을 가져온다.
		            rs.getString("seller_id"),
		            rs.getString("pname"),
		            rs.getString("kind"),
		            rs.getInt("price"),
		            rs.getString("content"),
		            rs.getString("useyn"),
		            rs.getString("regdate")
		        );
			    lists.add(product); //각 User객체를 ArrayList에 추가
			  }
			} finally {
			  DBUtil.close(con, pstmt, rs);
			} return lists;
			}
	  
//	  5.아이디별 모든 물품 조회
	  public static ArrayList<ProductDTO> searchProductId(String id) throws SQLException {
			Connection con = null;
			PreparedStatement pstmt = null;
			ResultSet rs = null;  //ResultSet :: select 문을 실행했을 경우 데이터베이스에서 결과를 받아와 저장하는 객체이다.
			ArrayList<ProductDTO> lists = new ArrayList<ProductDTO>(); //반환할 모든 Seller객체 정보를 담을 ArrayList 생성
			try {
			  con = DBUtil.getConnection();
			  pstmt = con.prepareStatement("SELECT * FROM product WHERE seller_id =?");
			  // id로 검색
			  pstmt.setString(1, id);
			  
			  rs = pstmt.executeQuery();
			  while (rs.next()) { // .next() : 수행결과로 ResultSet객체에서 하나의 Row를 반환한다. 더이상 결과가 없을 경우 false를 반환하면서 리턴
			                      // next()메소드를 한번 호출할때마다 한개의 레코드를 아이템으로 가진 객체를 반환한다.
			
			    ProductDTO product = new ProductDTO(
		    		rs.getInt("prodNum"), //ResultSet에서 getString()을 사용하여 각각의 컬럼의 값을 가져온다.
		            rs.getString("seller_id"),
		            rs.getString("pname"),
		            rs.getString("kind"),
		            rs.getInt("price"),
		            rs.getString("content"),
		            rs.getString("useyn"),
		            rs.getString("regdate")
		        );
			    lists.add(product); //각 User객체를 ArrayList에 추가
			  }
			} finally {
			  DBUtil.close(con, pstmt, rs);
			} return lists;
			}
	
	  
//	  6.검색한 모든 물품 조회
	  public static ArrayList<ProductDTO> searchProductPname(String pname) throws SQLException {
			Connection con = null;
			PreparedStatement pstmt = null;
			ResultSet rs = null;  //ResultSet :: select 문을 실행했을 경우 데이터베이스에서 결과를 받아와 저장하는 객체이다.
			ArrayList<ProductDTO> lists = new ArrayList<ProductDTO>(); //반환할 모든 Seller객체 정보를 담을 ArrayList 생성
			try {
			  con = DBUtil.getConnection();
			  pstmt = con.prepareStatement("SELECT * FROM product WHERE pname =?");
			  // pname으로 검색
			  pstmt.setString(1, pname);
			  
			  rs = pstmt.executeQuery();
			  while (rs.next()) { // .next() : 수행결과로 ResultSet객체에서 하나의 Row를 반환한다. 더이상 결과가 없을 경우 false를 반환하면서 리턴
			                      // next()메소드를 한번 호출할때마다 한개의 레코드를 아이템으로 가진 객체를 반환한다.
			
			    ProductDTO product = new ProductDTO(
		    		rs.getInt("prodNum"), //ResultSet에서 getString()을 사용하여 각각의 컬럼의 값을 가져온다.
		            rs.getString("seller_id"),
		            rs.getString("pname"),
		            rs.getString("kind"),
		            rs.getInt("price"),
		            rs.getString("content"),
		            rs.getString("useyn"),
		            rs.getString("regdate")
		        );
			    lists.add(product); //각 User객체를 ArrayList에 추가
			  }
			} finally {
			  DBUtil.close(con, pstmt, rs);
			} return lists;
			}
	  
	  
//	  7.검색한 모든 물품 조회
	  public static ArrayList<ProductDTO> searchProductKind(String kind) throws SQLException {
			Connection con = null;
			PreparedStatement pstmt = null;
			ResultSet rs = null;  //ResultSet :: select 문을 실행했을 경우 데이터베이스에서 결과를 받아와 저장하는 객체이다.
			ArrayList<ProductDTO> lists = new ArrayList<ProductDTO>(); //반환할 모든 Seller객체 정보를 담을 ArrayList 생성
			try {
			  con = DBUtil.getConnection();
			  pstmt = con.prepareStatement("SELECT * FROM product WHERE kind =?");
			  // kind로 검색
			  pstmt.setString(1, kind);
			  
			  rs = pstmt.executeQuery();
			  while (rs.next()) { // .next() : 수행결과로 ResultSet객체에서 하나의 Row를 반환한다. 더이상 결과가 없을 경우 false를 반환하면서 리턴
			                      // next()메소드를 한번 호출할때마다 한개의 레코드를 아이템으로 가진 객체를 반환한다.
			
			    ProductDTO product = new ProductDTO(
		    		rs.getInt("prodNum"), //ResultSet에서 getString()을 사용하여 각각의 컬럼의 값을 가져온다.
		            rs.getString("seller_id"),
		            rs.getString("pname"),
		            rs.getString("kind"),
		            rs.getInt("price"),
		            rs.getString("content"),
		            rs.getString("useyn"),
		            rs.getString("regdate")
		        );
			    lists.add(product); //각 User객체를 ArrayList에 추가
			  }
			} finally {
			  DBUtil.close(con, pstmt, rs);
			} return lists;
			}
	  
	  
	  
//	  7. 상품 삭제
	  public static boolean deleteUser(String id, int prodNum) throws SQLException {
		    Connection con = null;
		    PreparedStatement pstmt = null;
		    System.out.println("물품 삭제를 진행 중입니다.");
		    try {
		      con = DBUtil.getConnection();
		      pstmt = con.prepareStatement("DELETE FROM product WHERE seller_id =? and prodNum =?");
		      pstmt.setString(1, id);
		      pstmt.setInt(2, prodNum);
		      int result = pstmt.executeUpdate();
		      if (result == 1) {
		    	 System.out.println("물품 삭제가 완료되었습니다.");
		        return true;
		      }
		    } finally {
		      DBUtil.close(con, pstmt);
		    } return false;
		  }
	  
}
