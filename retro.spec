%global debug_package %{nil}

Summary: A language with roots in Forth
Name: retro
Version: 11.6
Release: 4.1
License: Freeware
Group: Development/Language
URL: http://www.forthworks.com/retro
Source0: http://s3.retroforth.org/download/11.x/%{name}-%{version}.tar.gz

%description
Retro is a concatenative, stack based language with roots in Forth. It is
designed to be small, easily learned, and easily modified to meet specific
needs, it has been developed and refined through continual use by a small
community over the last decade.

%prep
%setup -q

%build
make

%install
rm -rf ${RPM_BUILD_ROOT}
install -Dm755 %{name} ${RPM_BUILD_ROOT}%{_bindir}/%{name}

%clean
rm -rf ${RPM_BUILD_ROOT}

%files
%doc *.rst NOTES LICENSE
%{_bindir}/*

%changelog
* Tue Jul 28 2015 Wei-Lun Chao <bluebat@member.fsf.org> - 11.6
- Rebuild for Fedora
