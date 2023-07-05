%undefine _debugsource_packages

Name: daScript
Summary: High-performance statically strong typed scripting language
Version: 0.4
Release: 1
Group: Development/Languages
License: BSD-3-Clause
URL: https://dascript.org/
Source0: https://github.com/GaijinEntertainment/daScript/archive/refs/heads/master.zip#/%{name}-master.zip
BuildRequires: gcc-c++

%description
daScript is high-performance statically strong typed scripting language,
designed to be data-oriented embeddable ‘scripting’ language for performance
critical applications (like games or back-end/servers).

%prep
%setup -q -n %{name}-master
#sed -i '16i #include <thread>' examples/test/test_threads.cpp

%build
cmake . -DCMAKE_INSTALL_PREFIX=/usr
make %{?_smp_mflags}

%install
#make_install
install -d %{buildroot}%{_datadir}/%{name}
cp -a dasgen daslib include modules %{buildroot}%{_datadir}/%{name}
install -Dm755 bin/%{name} %{buildroot}%{_bindir}/%{name}

%files
%doc LICENSE README.md
%{_bindir}/%{name}
%{_datadir}/%{name}

%changelog
* Sun Jul 02 2023 Wei-Lun Chao <bluebat@member.fsf.org> - 0.4
- Rebuilt for Fedora
