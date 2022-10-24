package b2c_dto;



public class UserDTO {
  // user가 갖는 속성 : id, pw, nickname, name, phonenumber, ssn, address, business_number, user_type(enum "C" or "S")

  public enum UserType{
	    C("소비자"),
	    S("판매자");
	    ;
	  	
	  	//파이널 필드를 생성해 라벨 값 생성.
	    private final String label;

	    UserType(String label) {
	        this.label = label;
	    }

	    public String label() {
	        return label;
	    }} 

  private String id;
  private String pw;
  private String nickname;
  private String name;
  private String phonenumber;
  private String ssn;
  private String address;
  private String business_number; 
  public UserType userType;
  
  // 모든 회원 조회를 위한 함수
  public UserDTO(String string, String string2, String string3, String string4, String string5, String string6,
		String string7, String string8, String string9) {
	  this.id = string;
	    this.pw = string2;
	    this.nickname = string3;
	    this.name = string4;
	    this.phonenumber = string5;
	    this.ssn = string6;
	    this.address = string7;
	    this.business_number = string8;
	    
	    switch(string9) {
	      case "C":
	        this.userType = UserType.C;
	        break;
	      case "S":
	        this.userType = UserType.S;
	        break;
	      case "판매자" :
	    	this.userType = UserType.S;
	    	break;
	      case "null":
	    	this.userType = UserType.C;
	    	break;
	      default:
	        this.userType = UserType.C;
	        break;
	    }
	  
}

 
  // 유저 생성 함수
public UserDTO(String id, String pw, String nickname, String name, String phonenumber, String ssn, String address) {
	  this.id = id;
	    this.pw = pw;
	    this.nickname = nickname;
	    this.name = name;
	    this.phonenumber = phonenumber;
	    this.ssn = ssn;
	    this.address = address;

  }
  
  public String getId() {
    return id;
  }

  public void setId(String id) {
    this.id = id;
  }

  public String getPw() {
    return pw;
  }

  public void setPw(String pw) {
    this.pw = pw;
  }

  public String getNickname() {
    return nickname;
  }

  public void setNickname(String nickname) {
    this.nickname = nickname;
  }

  public String getName() {
    return name;
  }

  public void setName(String name) {
    this.name = name;
  }

  public String getPhonenumber() {
    return phonenumber;
  }

  public void setPhonenumber(String phonenumber) {
    this.phonenumber = phonenumber;
  }

  public String getSSN() {
    return ssn;
  }

  public void setSSN(String ssn) {
    this.ssn = ssn;
  }

  public String getAddress() {
    return address;
  }

  public void setAddress(String address) {
    this.address = address;
  }

  public String getBusiness_number() {
    return business_number;
  }

  public void setBusiness_number(String business_number) {
    this.business_number = business_number;
  }

  public String getSsn() {
    return ssn;
  }

  public void setSsn(String ssn) {
    this.ssn = ssn;
  }

  public UserType getUserType() {
    return userType;
  }

  public void setUserType(UserType userType) {
    this.userType = userType;
  }

  @Override
  public String toString() {
    return "유저 정보 [ 유저 아이디 = " + id + ", 유저 비밀번호  = " + pw + ", 닉네임 = " + nickname + ", 존함 = " + name + ", 휴대폰번호 = "
        + phonenumber + ", 주민등록번호 = " + ssn + ", 주소 = " + address + ", 사업자 등록번호 = " + business_number + ", 회원 정보 = "
        + userType.label() + " ]";
  }
}