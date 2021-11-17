%undefine _debugsource_packages

Name:		mlogo
Version:	0.0git
Release:	7.1
Summary:	A simple Logo Interpreter inspired by UCBLogo
License:	Open Source
Group:		Development/Languages
Source0:	%{name}-master.zip
URL:		https://github.com/iceseyes/mlogo
BuildRequires:	cmake
BuildRequires:  boost-devel
BuildRequires:  SDL2-devel

%description
A simple Logo Language Interpreter inspired by UCB Logo.

%prep
%setup -q -n %{name}-master

%build
cmake -DWITH_TESTS=OFF
%make_build

%install
rm -rf $RPM_BUILD_ROOT
install -Dm755 %{name} %{buildroot}%{_bindir}/%{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%doc README.md
%{_bindir}/%{name}

%changelog
* Wed Sep 12 2018 Wei-Lun Chao <bluebat@member.fsf.org> - 0.0git
- Rebuilt for Fedora
