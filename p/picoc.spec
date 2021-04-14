Summary:	A very small C interpreter
Name:		picoc
Version:	2.2
Release:	2.1
License:	New BSD
Group:		Development/C
URL:		https://github.com/zsaleeba/picoc
Source0:    %{name}-master.zip
BuildRequires: readline-devel

%description
PicoC is a very small C interpreter for scripting. It was originally written
as the script language for a UAV's on-board flight system. It's also very
suitable for other robotic, embedded and non-embedded applications.

%prep
%setup -q -n %{name}-master
sed -i 's|`svnversion -n`|%{version}|' Makefile

%build
make

%install
rm -rf $RPM_BUILD_ROOT
install -Dm755 %{name} $RPM_BUILD_ROOT%{_bindir}/%{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%doc README
%{_bindir}/%{name}

%changelog
* Fri Nov 10 2017 Wei-Lun Chao <bluebat@member.fsf.org> - 2.2
- Rebuilt for Fedora
