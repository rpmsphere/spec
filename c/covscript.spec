%undefine _debugsource_packages

Summary: Covariant Script Interpreter
Name: covscript
Version: 3.4.1.16
Release: 1
License: Apache 2.0
Group: Development/Languages
#Source0: https://github.com/covscript/covscript/archive/refs/tags/%{version}.tar.gz#/%{name}-%{version}.tar.gz
Source0: %{name}-master.zip
URL: https://github.com/covscript/covscript/

%description
Covariant Script is an open source, cross-platform programming language.

%prep
%setup -q -n %{name}-master

%build
%cmake
%cmake_build

%install
#cmake_install
install -d %{buildroot}%{_bindir} %{buildroot}%{_datadir}/%{name} %{buildroot}%{_libdir}/%{name} %{buildroot}%{_includedir}
install -m755 *-linux-build/cs %{buildroot}%{_bindir}/%{name}
install -m755 *-linux-build/*.cse %{buildroot}%{_datadir}/%{name}
install -m644 *-linux-build/lib%{name}.a %{buildroot}%{_libdir}/%{name}
cp -a include/%{name} %{buildroot}%{_includedir}

%files 
%doc LICENSE *.md
%{_bindir}/%{name}
%{_datadir}/%{name}
%{_libdir}/%{name}
%{_includedir}/%{name}

%clean
rm -rf $RPM_BUILD_ROOT

%changelog
* Sun Oct 09 2022 Wei-Lun Chao <bluebat@member.fsf.org> - 3.4.1.16
- Rebuilt for Fedora
