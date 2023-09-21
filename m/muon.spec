%undefine _debugsource_packages

Summary: Modern low-level programming language
Name: muon
Version: 0.3.7git
Release: 1
License: MIT
Group: Development/Language
URL: https://github.com/nickmqb/muon
#Source0: https://codeload.github.com/nickmqb/muon/tar.gz/refs/tags/v%{version}#/%{name}-%{version}.tar.gz
Source0: %{name}-master.zip

%description
Muon is a modern low-level programming language, inspired by C, C#, Go, Rust and Python.

%prep
%setup -q -n %{name}-master

%build
make CFLAGS=-O3 ARCH=

%install
install -Dm755 bootstrap/mu %{buildroot}%{_bindir}/%{name}
install -d %{buildroot}%{_datadir}/%{name}
cp -a examples lib %{buildroot}%{_datadir}/%{name}

%clean
rm -rf ${RPM_BUILD_ROOT}

%files
%doc LICENSE *.md
%{_bindir}/%{name}
%{_datadir}/%{name}

%changelog
* Sun Sep 17 2023 Wei-Lun Chao <bluebat@member.fsf.org> - 0.3.7git
- Rebuilt for Fedora
