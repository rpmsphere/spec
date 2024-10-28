%undefine _debugsource_packages

Name: ospedit
Version: 2.1.1
Release: 9.3
Summary: OSPlus Text Editor
License: GPLv2
Group: Development/Languages
URL: https://osplus.sourceforge.net/
Source0: https://sourceforge.net/projects/osplus/files/Text%20Editor/%{version}/%{name}-%{version}-src.zip
BuildRequires: dos2unix
BuildRequires: rhtvision-devel
BuildRequires: gpm-devel
BuildRequires: allegro-devel

%description
A text editor included in OSPlus.

%prep
%setup -q
dos2unix configure
sed -i 's|sys_errlist\[errno\]|strerror(errno)|' src/convert/txtwrite.c

%build
sh configure linux
make

%install
install -d %{buildroot}%{_bindir}
install -m755 bin/linux/* %{buildroot}%{_bindir}

%files
%doc *.txt docs/*.txt
%{_bindir}/*

%changelog
* Fri Feb 07 2014 Wei-Lun Chao <bluebat@member.fsf.org> - 2.1.1
- Rebuilt for Fedora
