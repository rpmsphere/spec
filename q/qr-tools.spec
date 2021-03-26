Name:		qr-tools
Version:	1.2
Release:	2.1
Summary:	A suite of tools for handling QR codes
Group:		Development/Tools
License:	GPLv3
URL:		https://launchpad.net/qr-tools
Source0:	https://launchpad.net/qr-tools/trunk/%{version}/+download/%{name}-%{version}.tar.gz

%description
QR Tools project is formed by the python-qrtools and QtQR.

%package -n python-qrtools
Summary: A high level library for reading and generating QR codes
Requires: qrencode, PyQt4, zbar-pygtk, python-imaging
BuildArch: noarch

%description -n python-qrtools
A backend ("library") for creating and decoding QR Codes in python.
Depends on qrenconde and zbar. You can use it in your own projects.

%package -n qtqr
Summary: A Graphical interface QR Code generator and decoder
Requires: python-qrtools
BuildArch: noarch

%description -n qtqr
A Qt GUI (front-end) for python-qrtools that makes easy creating and decoding the codes.

%prep
%setup -q -n %{name}

%install
rm -rf $RPM_BUILD_ROOT
install -Dm644 qrtools.py $RPM_BUILD_ROOT%{python3_sitelib}/qrtools.py
mkdir -p $RPM_BUILD_ROOT%{_bindir}
cat > $RPM_BUILD_ROOT%{_bindir}/%{name} << EOF
#!/usr/bin/bash
cd %{_datadir}/%{name}
./%{name}.py
EOF

mkdir -p $RPM_BUILD_ROOT%{_datadir}/%{name}
cp -a *.py *.qm $RPM_BUILD_ROOT%{_datadir}/%{name}
install -Dm644 icon.png $RPM_BUILD_ROOT%{_datadir}/pixmaps/%{name}.png
mkdir -p $RPM_BUILD_ROOT%{_datadir}/applications
cat > $RPM_BUILD_ROOT%{_datadir}/applications/%{name}.desktop << EOF
[Desktop Entry]
Encoding=UTF-8
Comment=GUI front-end for qrencode
Name=QtQR
Type=Application
Exec=%{name}
Icon=%{name}
Categories=Application;Utility;
EOF

sed -i 's|/usr/bin/env python$|/usr/bin/python3|' %{buildroot}%{_datadir}/%{name}/*.py

%clean
rm -rf $RPM_BUILD_ROOT

%files -n python-qrtools
%doc LICENCE samples
%{python3_sitelib}/qrtools.py*
%{python3_sitelib}/__pycache__/*

%files -n qtqr
%{_bindir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/pixmaps/%{name}.png
%{_datadir}/%{name}

%changelog
* Thu Jun 15 2017 Wei-Lun Chao <bluebat@member.fsf.org> - 1.2
- Rebuild for Fedora
