Name:          pyslsk
Version:       1.2.7c
Release:       10.1
Summary:       A client for SoulSeek filesharing system
Group:         Graphical Desktop/Applications/Internet
URL:           http://www.sensi.org/~ak/pyslsk/
Source0:       http://www.sensi.org/%7Eak/pyslsk/pyslsk-%{version}.tar.gz
Source1:       slsk.png
License:       GPL
BuildArch:     noarch
Requires:      python2-vorbis
BuildRequires: python2-devel

%description
A client for SoulSeek filesharing system.

%prep
%setup -q

%build
python2 setup.py build

%install
rm -rf $RPM_BUILD_ROOT
python2 setup.py install --root=$RPM_BUILD_ROOT --install-headers=%{_includedir}/python2.7 --install-lib=%{python2_sitelib}
sed -i 's|RELEASE_NUMBER|RELEASE_VERSION|' $RPM_BUILD_ROOT%{_bindir}/%{name}
install -Dm644 %{SOURCE1} $RPM_BUILD_ROOT%{_datadir}/pixmaps/slsk.png
mkdir -p $RPM_BUILD_ROOT%{_datadir}/applications
cat > $RPM_BUILD_ROOT%{_datadir}/applications/pyslsk.desktop << EOF
[Desktop Entry]
Name=pyslsk
GenericName=SoulSeek filesharing system client
GenericName[it]=Client SoulSeek per la condivisione file 
Exec=pyslsk
Type=Application
Terminal=false
Categories=Network;P2P;
Icon=slsk
EOF

sed -i 's|/usr/bin/python$|/usr/bin/python2|' %{buildroot}%{_bindir}/%{name}*
   
%clean
rm -rf $RPM_BUILD_ROOT

%files
%{_bindir}/*
%{python2_sitelib}/pysoulseek*
%{python2_sitelib}/pyslsk*
%{_datadir}/applications/pyslsk.desktop
%{_datadir}/pixmaps/slsk.png

%changelog
* Mon Feb 01 2016 Wei-Lun Chao <bluebat@member.fsf.org> - 1.2.7c
- Rebuild for Fedora
* Sat Oct 04 2008 Tiziana Ferro <tiziana.ferro@email.it> 1.2.7b-4mamba
- update system menu entry
- added autobuildreq
* Tue Aug 09 2005 Silvan Calarco <silvan.calarco@qilinux.it> 1.2.7b-3qilnx
- rebuild in site-python dir
* Fri May 13 2005 Silvan Calarco <silvan.calarco@qilinux.it> 1.2.7b-2qilnx
- added desktop menu entry
* Wed May 11 2005 Silvan Calarco <silvan.calarco@qilinux.it> 1.2.7b-1qilnx
- package created by autospec
