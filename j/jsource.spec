%undefine _debugsource_packages

Summary: J engine source mirror
Name: jsource
Version: 9.6
Release: 1
License: GPL3
Group: Development/Languages
Source: %{name}-build96.tar.gz
URL: https://github.com/jsoftware/jsource

%description
J is a high-level, general-purpose programming language that is particularly
suited to the mathematical, statistical, and logical analysis of data. It is
a powerful tool for developing algorithms and exploring problems that are not
already well understood.

%prep
%setup -q -n %{name}-build96
sed -i '/-Wno-unknown-warning-option/d' make2/*.sh

%build
make2/build_all.sh

%install
rm -rf $RPM_BUILD_ROOT
install -Dm755 bin/linux/j64avx2/jconsole %{buildroot}%{_bindir}/ijconsole
install -Dm644 bin/linux/j64avx2/libj.so %{buildroot}%{_libdir}/libj.so
ln -s libj.so %{buildroot}%{_libdir}/libj.so.%{version}
install -Dm644 bin/linux/j64avx2/libtsdll.so %{buildroot}%{_libdir}/libtsdll.so
ln -s libtsdll.so %{buildroot}%{_libdir}/libtsdll.so.%{version}
install -d %{buildroot}%{_datadir}/j/%{version}
cp -a jlibrary/{system,addons} %{buildroot}%{_datadir}/j/%{version}
install -Dm644 jlibrary/bin/profile.ijs %{buildroot}%{_sysconfdir}/j/%{version}

%files 
%doc *.txt
%{_bindir}/ijconsole
%{_libdir}/lib*
%{_datadir}/j/%{version}
%{_sysconfdir}/j/%{version}

%changelog
* Sun Apr 20 2025 Wei-Lun Chao <bluebat@member.fsf.org> - 9.6
- Rebuilt for Fedora
