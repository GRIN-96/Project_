package dbutil;

import java.io.FileInputStream;
import java.io.IOException;
import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.ResultSet;
import java.sql.SQLException;
import java.sql.Statement;
import java.util.Properties;

public class DBUtil {
   // DB 설정
   static Properties propertiesInfo = new Properties(); 
   static {
      try {
         propertiesInfo.load( new FileInputStream("db.properties") ); //db.properties 문서에 있는 값을 propertiesInfo에 반영시킨다. db.properties에는 db에 접속하기 위한 URL, USER, PASSWORD 를 기입해뒀다.
         Class.forName(propertiesInfo.getProperty("jdbc.driver")); // 드라이버의 클래스를 등록
            // propertiesInfo.getProperty()가 'jdbc.driver'에 해당하는 값을 반환 ("com.mysql.cj.jdbc.Driver") -> Class.forName()의 매개변수로 넘겨서 해당 이름을 갖는 클래스를 메모리로 로딩
      } catch (Exception e) {
         e.printStackTrace();
      }
   }
   
   public static Connection getConnection() throws SQLException {  // DB연결 해주는 메소드
      return DriverManager.getConnection(propertiesInfo.getProperty("jdbc.url"),    
                                 propertiesInfo.getProperty("jdbc.id"), 
                                 propertiesInfo.getProperty("jdbc.pw")); //위 값을 이용해서 DB 연결
   }

   // 자원반환
   public static void close(Connection con, Statement stmt, ResultSet rset) { // 쿼리 진행 후 사용한 자원을 반납하기 위한 메소드
      try {
         if (rset != null) {
            rset.close();
            rset = null;
         }
         if (stmt != null) {
            stmt.close();
            stmt = null;
         }
         if (con != null) {
            con.close();
            con = null;
         }
      } catch (SQLException e) {
         e.printStackTrace();
      }
   }

   // 자원반환
   public static void close(Connection con, Statement stmt) { // 자원반환 메소드를 두개의 argument만 받을 수 있도록 오버로딩
      try {
         if (stmt != null) {
            stmt.close();
            stmt = null;
         }
         if (con != null) {
            con.close();
            con = null;
         }
      } catch (SQLException e) {
         e.printStackTrace();
      }
   }
}