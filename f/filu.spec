Name: filu
Summary: Supports Your Stock Trading
Version: 2013.08.30
Release: 11.1
Group: Applications/Productivity
License: GPLv2
URL: http://filu.sourceforge.net/
Source0: http://sourceforge.net/projects/filu/files/filu-snapshot-2013-08-30.tar.gz
BuildRequires: cmake
BuildRequires: qt-devel
BuildRequires: qt-postgresql
BuildRequires: libpq-devel
BuildRequires: muParser-devel
BuildRequires: ta-lib-devel

%description
Filu is aimed to support your stock trading. Some of its features are:
Market Scanner, Indicator scripting, TA-Lib support, Postgres driven FIs
and indicators, Trading scripting, Backtester with optimizer functionality.

%prep
%setup -q -n FiluSource-2013-08-30
sed -i '/ReqPostgreSqlVersion/d' libs/qt-psqldriver/CMakeLists.txt

%build
%cmake
make %{?_smp_mflags}

%install
%make_install
%ifarch x86_64 aarch64
mv %{buildroot}/usr/lib %{buildroot}/usr/lib64
%endif
sed -i 's|/usr/share/icons/hicolor/48x48/apps/||' $RPM_BUILD_ROOT%{_datadir}/applications/%{name}-*.desktop

%post
/usr/sbin/ldconfig %{_libdir}/Filu

%postun
/usr/sbin/ldconfig

%files
%{_datadir}/doc/Filu
%{_bindir}/*
%{_sysconfdir}/Filu.conf
%{_sysconfdir}/ld.so.conf.d/Filu.conf
%{_libdir}/Filu
%{_datadir}/applications/filu-*.desktop
%{_datadir}/icons/hicolor/48x48/apps/*.png

%changelog
* Wed Dec 11 2013 Wei-Lun Chao <bluebat@member.fsf.org> - 2013.08.30
- Rebuild for Fedora
