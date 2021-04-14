%undefine _debugsource_packages
%define pkg_name pyNeighborhood

Name: pyneighborhood
Version: 0.5.0
Release: 1
License: GPL
Group: Networking/File transfer
Summary: Samba share browser
Source: http://downloads.sourceforge.net/pyneighborhood/%{name}-%{version}-rc2.tar.bz2
URL: http://pyneighborhood.sourceforge.net/
Requires: pygtk2, samba-client
BuildArch: noarch
Vendor: Mykola Lynnyk (definer)

%description
pyNeighborhood is GTK+2 rewrite of a well-known GTK+1 tool
LinNeighborhood(using pyGTK), so it is the GUI frontend for
samba tools, such as smbclient, smbmount etc. It's written in
Python and uses the GTK+2 toolkit with pyGTK implementation. 

%prep
%setup -q -n %{name}-%{version}-rc2
echo -e 'Name[zh_TW]=巨蠎網路芳鄰\nComment[zh_TW]=PyGTK 編寫的 SMB 資源分享瀏覽器' >> %{pkg_name}.desktop 
sed -i '/#~/d' po/es_ES.po

%build
python2 setup.py build
%__make -C po

%install
%__rm -rf %{buildroot}
python2 setup.py install --root=%{buildroot}
%__make DESTDIR=%{buildroot} -C po install

sed -i 's|/usr/bin/python |/usr/bin/python2 |' %{buildroot}%{_bindir}/*

%clean
%__rm -rf %{buildroot}

%files
%doc COPYING README Changelog
%{_bindir}/%{pkg_name}
%{_datadir}/applications/%{pkg_name}.desktop
%{_datadir}/%{name}
%{_datadir}/locale/*/LC_MESSAGES/*
%{python2_sitelib}/pyneighborhood*
%exclude %{_docdir}/pyneighborhood

%changelog
* Tue Mar 20 2018 Wei-Lun Chao <bluebat@member.fsf.org> - 0.5.0
- Rebuilt for Fedora
