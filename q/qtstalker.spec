Name:			qtstalker
Summary:		A user friendly Technical Analysis package
Version:		0.36
Release:		48.1
License:		GPL
Group:			Productivity/Office/Finance
URL:			http://qtstalker.sourceforge.net/
Source:			%{name}-%{version}.tar.gz
Source1:		%{name}.png
#Source2:		%{name}.sh
Patch0:			%{name}-gcc43.patch
Patch1:			qtstalker-stringcompare.patch
BuildRequires: gcc-c++
BuildRequires:  libdb-devel
BuildRequires:	ta-lib-devel
BuildRequires:	qt3-devel

%description
Qtstalker is a user friendly Technical Analysis package for GNU/Linux
(and hence other Unix-like systems). Similar to commercial wares such
as Metastock, Supercharts and Tradestation. Keeps to a lean, simple
design for speed, portability, and low resource usage. Because it
uses a plugin model, Qtstalker can easily be extended.

Qtstalker is 100% free software, distributed under the terms of the
GNU GPL. An active development community is continually adding new
features. We appreciate your input towards creating a world-class
GNU/Linux TA package.

%prep
%setup -q -n %{name}
%patch0 -p1
%patch1 -p1
sed -i 1i\ '#include <unistd.h>' lib/ExScript.cpp
sed -i -e 's|/usr/local/lib|%{_libdir}|g' lib/RcFile.cpp lib/Config.cpp lib/lib.pro
sed -i -e 's|/usr/local|/usr|g' lib/RcFile.cpp lib/Config.cpp src/Qtstalker.cpp docs/docs.pro plugins/quote/*/*.pro src/src.pro lib/lib.pro
sed -i -e 's|-ldb|-L%{_libdir}/libdb4 -ldb|' -e '163i unix:INCLUDEPATH += /usr/include/libdb4' lib/lib.pro
sed -i -e 's|-L\.\./lib|-L%{_libdir}/libdb4 -L../lib|' -e '53i INCLUDEPATH += /usr/include/libdb4' src/src.pro
sed -i -e '12i LIBS += -L%{_libdir}/libdb4' -e '10i INCLUDEPATH += /usr/include/libdb4' plugin.config
sed -i 's|qDebug(|qDebug("%%s", |' plugins/quote/CME/CME.cpp

%build
export QTDIR=%{_libdir}/qt-3.3
export PATH=$QTDIR/bin:$PATH
%configure ||:
make

%install
%__rm -rf %{buildroot}
%__install -Dm755 lib/libqtstalker.so.0.36.0 %{buildroot}%{_libdir}/libqtstalker.so.0.36.0
ln -s libqtstalker.so.0.36.0 %{buildroot}%{_libdir}/libqtstalker.so
ln -s libqtstalker.so.0.36.0 %{buildroot}%{_libdir}/libqtstalker.so.0
ln -s libqtstalker.so.0.36.0 %{buildroot}%{_libdir}/libqtstalker.so.0.36
%__install -Dm755 src/%{name} %{buildroot}%{_bindir}/%{name}
%__install -d %{buildroot}%{_libdir}/%{name}/quote
%__install -m755 plugins/quote/*/lib*.0.36.so %{buildroot}%{_libdir}/%{name}/quote
%__install -d %{buildroot}%{_datadir}/%{name}/i18n
%__install -m644 i18n/%{name}_*.qm %{buildroot}%{_datadir}/%{name}/i18n
%__install -d %{buildroot}%{_datadir}/%{name}/indicator
%__install -m644 misc/CUS_examples/{bar,cdl-rel,cdl-rel-ma,RSI,STOCH,VOL} %{buildroot}%{_datadir}/%{name}/indicator

# icon
%__install -Dm 644 %{SOURCE1} %{buildroot}%{_datadir}/pixmaps/%{name}.png

# menu
%__install -dm 755 %{buildroot}%{_datadir}/applications
%__cat > %{buildroot}%{_datadir}/applications/%{name}.desktop << EOF
[Desktop Entry]
Comment=An user friendly Technical Analysis package
Name=Qtstalker
Type=Application
Exec=%{name}
Icon=%{name}
Terminal=false
Categories=Office;Finance;
Encoding=UTF-8
EOF

%clean
%__rm -rf %{buildroot}

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files
%doc docs/*
%{_bindir}/%{name}
%{_libdir}/libqtstalker.so*
%{_libdir}/%{name}
%{_datadir}/%{name}
%{_datadir}/applications/%{name}*.desktop
%{_datadir}/pixmaps/%{name}.png

%changelog
* Sun Jan 06 2013 Wei-Lun Chao <bluebat@member.fsf.org> - 0.36
- Rebuilt for Fedora
* Thu May 01 2008 Toni Graffy <toni@links2linux.de> - 0.36-0.pm.1
- update to 0.36
* Fri Sep 28 2007 Toni Graffy <toni@links2linux.de> - 0.35-0.pm.1
- initial release of rpm 0.35
