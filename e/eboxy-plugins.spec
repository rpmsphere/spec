Name: eboxy-plugins
Version: 0.4.0
Release: 3
URL: http://eboxy.sourceforge.net
License: GPLv2
Summary: Plugins for eboxy
Group: Applications/Multimedia
Source0: http://eboxy.sourceforge.net/eboxy-plugins-%{version}.tar.gz
BuildRequires: eboxy-devel mysql-devel
BuildRequires: libtool readline-devel ncurses-devel xine-lib-devel
#BuildRequires: lm_sensors-devel xmms-devel

%description
Provides plugins for eboxy.

%prep
%setup -q -n %{name}
grep -rl /usr/local . | xargs sed -i -e's,/usr/local,/usr,g'
grep -rl lib/ . | xargs sed -i -e's,lib/,%{_lib}/,g'
sed -i -e's,linux/sensors,sensors/sensors,g' hwsensors/hwsensors.c

%build
pushd mysql
make
popd
pushd playlist
make
popd
pushd rcon
make
popd
pushd xine
make
popd
#pushd xmmsctrl
#make
#popd
#pushd hwsensors
#make
#popd

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}%{_libdir}/eboxy/plugins/generic
#install -m755 $RPM_BUILD_DIR/%{name}/hwsensors/hwsensors.so %{buildroot}%{_libdir}/eboxy/plugins/generic
install -m755 $RPM_BUILD_DIR/%{name}/playlist/playlist.so   %{buildroot}%{_libdir}/eboxy/plugins/generic
install -m755 $RPM_BUILD_DIR/%{name}/xine/xine.so           %{buildroot}%{_libdir}/eboxy/plugins/generic
#install -m755 $RPM_BUILD_DIR/%{name}/xmmsctrl/xmmsctrl.so   %{buildroot}%{_libdir}/eboxy/plugins/generic
install -m755 $RPM_BUILD_DIR/%{name}/rcon/rcon.so           %{buildroot}%{_libdir}/eboxy/plugins/generic
install -m755 $RPM_BUILD_DIR/%{name}/mysql/mysql.so         %{buildroot}%{_libdir}/eboxy/plugins/generic

%clean
rm -rf %{buildroot}

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files
%defattr (-,root,root)
%doc hwsensors/hwsensors.txt playlist/playlist.txt xine/xine.txt
%doc xmmsctrl/xmmsctrl.txt rcon/rcon.txt mysql/mysql.txt
%{_libdir}/eboxy/plugins/generic/*

%changelog
* Tue Mar 20 2018 Wei-Lun Chao <bluebat@member.fsf.org> - 
- Rebuilt for Fedora
* Thu Dec 25 2008 Wei-Lun Chao <bluebat@member.fsf.org> 0.4.0-3.ossii
- Rebuild for OSSII

* Sat Dec 13 2008 Paulo R. Cavalcanti <roma@lcg.ufrj.br> 0.4.0-3
- Not building lm_sensors plugin for Fedora 10.

* Wed Apr 18 2007 Paulo R. Cavalcanti <roma@lcg.ufrj.br> 0.4.0-2
- Rebuilt for Fedora 6.

* Tue Aug 19 2004 Paulo R. Cavalcanti <roma@lcg.ufrj.br> 0.4.0-1
- Created initial rpm.
