%undefine _debugsource_packages

Name:           pam_facialauth
License:        MIT
Group:          System/Libraries
Summary:        PAM facial authentication
Version:        0.20170509
Release:        6.1
Source:         pam-facial-auth-master.zip
URL:            https://github.com/devinaconley/pam-facial-auth
BuildRequires:  cmake atlas
BuildRequires:  pam-devel
BuildRequires:  opencv-devel
BuildRequires:  hdf5-devel

%description
A pluggable authentication module that relies on facial recognition to verify
the user attempting to gain access. Looks for a match between username and
label associated with the recognized face.

%prep
%setup -q -n pam-facial-auth-master
sed -i -e 's|fr->load|fr->read|' -e 's|cv::face::create\([a-zA-Z]*\)|cv::face::\1::create|' src/FaceRecWrapper.cpp
sed -i -e 's|CV_BGR2GRAY|6|' -e 's|CV_LOAD_IMAGE_GRAYSCALE|0|' src/FacialAuth.cpp run_training.cpp
sed -i 's|CV_HAAR_SCALE_IMAGE|2|' src/FaceRecWrapper.cpp

%build
cmake .
%make_build

%install
#make_install
install -Dm755 facialauth.so $RPM_BUILD_ROOT/%{_lib}/security/facialauth.so
install -Dm755 run_test $RPM_BUILD_ROOT%{_bindir}/pam_facial_auth_run_test
install -Dm755 run_training $RPM_BUILD_ROOT%{_bindir}/pam_facial_auth_run_training
install -Dm644 etc/haarcascade_frontalface_alt.xml $RPM_BUILD_ROOT/etc/pam-facial-auth/haarcascade_frontalface_alt.xml
install -Dm644 etc/haarcascade_frontalface_default.xml $RPM_BUILD_ROOT/etc/pam-facial-auth/haarcascade_frontalface_default.xml

%files
%doc README.md LICENSE
/%{_lib}/security/facialauth.so
%{_bindir}/pam_facial_auth_run_test
%{_bindir}/pam_facial_auth_run_training
/etc/pam-facial-auth/haarcascade_frontalface_alt.xml
/etc/pam-facial-auth/haarcascade_frontalface_default.xml

%changelog
* Fri Mar 16 2018 Wei-Lun Chao <bluebat@member.fsf.org> - 0.20170509
- Rebuilt for Fedora
