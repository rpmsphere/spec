Summary:       Free ePub Reader
Name:          azardi
Version:       6.0
Release:       1
Source0:       https://azardi-download.s3.amazonaws.com/AZARDI6_20110929_i386.deb
License:       shareware
Group:         Productivity/Other
BuildArch:     noarch
Requires:      xulrunner
URL:           https://azardi.infogridpacific.com/

%description
The AZARDI 6 release is a full reinvention of AZARDI and the eBook Reader.
This new version is built on the latest Mozilla framework and inherits all
the advanced features of Firefox 6.0.

%prep
%setup -T -c
ar -x %{SOURCE0}
tar xzf data.tar.gz

%build

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT%{_datadir}/%{name}
rm -rf opt/infogridpacific/azardi-6.0/xulrunner opt/infogridpacific/azardi-6.0/AZARDI6.desktop
cp -a opt/infogridpacific/azardi-6.0/* $RPM_BUILD_ROOT%{_datadir}/%{name}
mkdir -p $RPM_BUILD_ROOT%{_datadir}/doc
cp -a usr/share/doc/* $RPM_BUILD_ROOT%{_datadir}/doc

install -Dm644 usr/share/icons/azardi-6.0.png %{buildroot}%{_datadir}/pixmaps/azardi.png

%__mkdir_p %{buildroot}%{_datadir}/applications
cat > %{buildroot}%{_datadir}/applications/%{name}.desktop << EOF
[Desktop Entry]
Version=1.0
Encoding=UTF-8
Type=Application
Name=Azardi
Comment=Free ePub Reader
Exec=%{name}
Terminal=false
Categories=Utility;
Icon=azardi
EOF

%__mkdir_p %{buildroot}%{_bindir}
cat > %{buildroot}%{_bindir}/%{name} << EOF
#!/bin/sh
cd %{_datadir}/%{name}
xulrunner application.ini
EOF

%files
%attr(755,root,root) %{_bindir}/%{name}
%{_datadir}/doc/%{name}-%{version}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/%{name}
%{_datadir}/pixmaps/%{name}.png

%changelog
* Mon Feb 26 2018 Wei-Lun Chao <bluebat@member.fsf.org> - 6.0
- Rebuilt for Fedora
