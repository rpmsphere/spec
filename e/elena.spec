%undefine _debugsource_packages

Summary: The Elena Programming Language
Name: elena
Version: 5.10.0
Release: 1
License: MIT
Group: Development/Language
URL: https://elena-lang.github.io/
#Source0: https://github.com/ELENA-LANG/elena-lang/archive/refs/tags/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
Source0: elena-lang-master.zip

%description
ELENA is a general-purpose language with late binding. It is multi-paradigm,
combining features of functional and object-oriented programming. It supports
both strong and weak types, run-time conversions, boxing and unboxing primitive
types, direct usage of external libraries. A rich set of tools is provided to
deal with message dispatching : multi-methods, message qualifying, generic
message handlers. Multiple-inheritance can be simulated using mixins and type
interfaces. The built-in script engine allows incorporating custom-defined
scripts into your applications. Both stand-alone applications and Virtual
machine clients are supported.

%prep
%setup -q -n elena-lang-master
sed -i -e 's|-m32||' -e 's|-march=pentium2||' `find . -name *.mak`

%build
#cmake .
%make_build elc_lnx32

%install
#make_install
install -Dm755 bin/%{name}-lc %{buildroot}%{_bindir}/%{name}-lc
mkdir -p %{buildroot}%{_datadir}/%{name}
cp -a bin/templates bin/scripts %{buildroot}%{_datadir}/%{name}
install -m644 dat/sg/syntax.txt %{buildroot}%{_datadir}/%{name}/syntax.dat
install -m644 dat/og/rules.txt %{buildroot}%{_datadir}/%{name}/rules.dat
install -Dm644 bin/elc.config %{buildroot}%{_sysconfdir}/%{name}/elc.config

%clean
rm -rf ${RPM_BUILD_ROOT}

%files
%doc LICENSE *.md
%{_bindir}/%{name}-lc
%{_datadir}/%{name}
%{_sysconfdir}/%{name}

%changelog
* Sun Mar 27 2022 Wei-Lun Chao <bluebat@member.fsf.org> - 5.10.0
- Rebuilt for Fedora
