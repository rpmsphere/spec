%undefine _debugsource_packages

Summary: J engine source mirror
Name: jsource
Version: 9.04
Release: 0.beta
License: GPL3
Group: Development/Languages
Source: %{name}-master.zip
URL: https://github.com/jsoftware/jsource

%description
J is a high-level, general-purpose programming language that is particularly
suited to the mathematical, statistical, and logical analysis of data. It is
a powerful tool for developing algorithms and exploring problems that are not
already well understood.

%prep
%setup -q -n %{name}-master
sed -i '/-Wno-unknown-warning-option/d' make2/*.sh

%build
make2/build_all.sh

%install
rm -rf $RPM_BUILD_ROOT
install -Dm755 bin/linux/j64avx/jconsole %{buildroot}%{_bindir}/ijconsole
install -Dm644 bin/linux/j64avx/libj.so %{buildroot}%{_libdir}/libj.so
ln -s libj.so %{buildroot}%{_libdir}/libj.so.%{version}
install -Dm644 bin/linux/j64avx/libtsdll.so %{buildroot}%{_libdir}/libtsdll.so
ln -s libtsdll.so %{buildroot}%{_libdir}/libtsdll.so.%{version}
install -d %{buildroot}%{_datadir}/j/%{version}
cp -a jlibrary/{system,tools,addons} %{buildroot}%{_datadir}/j/%{version}
install -Dm644 jlibrary/bin/profile.ijs %{buildroot}%{_sysconfdir}/j/%{version}

%files 
%doc *.txt
%{_bindir}/ijconsole
%{_libdir}/lib*
%{_datadir}/j/%{version}
%{_sysconfdir}/j/%{version}

%changelog
* Sun Mar 20 2022 Wei-Lun Chao <bluebat@member.fsf.org> - 9.04.beta
- Rebuilt for Fedora
