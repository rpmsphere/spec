%global debug_package %{nil}
Name:           pam_face
Version:        1.0
Release:        9.1
Summary:        Linux Pluggable Authentication Module (PAM) for face authentication
License:        German Free Software License
Group:          System
URL:            https://github.com/philippmeisberger/pam-face
Source0:        pam-face-master.zip
BuildRequires:  python2-devel
Requires:       python2-opencv
Requires:       pam_python
BuildArch:      noarch

%description
PAM Face is a Linux Pluggable Authentication Module (PAM) for password-less
face authentication using OpenCV. Only a webcam is required. Per default the
password authentication is set as fallback. Two-factor authentication is also
possible. The module has to be configured by the pamface-conf program.

%prep
%setup -q -n pam-face-master
sed -i 's|/usr/share/opencv|/usr/share/OpenCV|' src/pamface/facerecognizer.py

%build
python2 setup.py build

%install
python2 setup.py install -O1 --root=%{buildroot} --prefix=/usr
#install -Dm644 debian/pam-auth-update/face %{buildroot}%{_datadir}/pam-configs/face
install -Dm644 src/pam_face.py %{buildroot}/lib/security/pam_face.py
install -Dm755 src/pamface-conf %{buildroot}%{_bindir}/pamface-conf
install -Dm644 src/pamface.conf %{buildroot}%{_sysconfdir}/pamface/pamface.conf
install -Dm644 src/models.xml %{buildroot}%{_sysconfdir}/pamface/models.xml

sed -i 's|/usr/bin/env python$|/usr/bin/python2|' %{buildroot}%{_bindir}/*

%post
#authconfig --enableface --update

%postun
#authconfig --disableface --update

%files
%doc README.md COPYING LICENSE
%{_bindir}/pamface-conf
#{_datadir}/pam-configs
/lib/security/pam_face.py*
%{_sysconfdir}/pamface
%{python2_sitelib}/pamface
%{python2_sitelib}/libpam_face*

%changelog
* Fri Mar 16 2018 Wei-Lun Chao <bluebat@member.fsf.org> - 1.0
- Rebuild for Fedora
