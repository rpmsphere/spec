%undefine _debugsource_packages

Name:                   duplo
Version:                0.2.0
Summary:                Finds duplicate code
License:                GPL
URL:                    https://sourceforge.net/projects/duplo/
Group:                  Development/Tools/Other
Release:                11.1
Source:                 %{name}-%{version}.tar.gz
BuildRequires:          gcc-c++

%description
Searches a list of files looking for duplicate code.

%prep
%setup -q
sed -i '19i #include <string.h>' Duplo.cpp

%build
%{__make} CFLAGS="%{optflags}"

%install
%{__rm} -rf $RPM_BUILD_ROOT
install -D -m755 %{name} $RPM_BUILD_ROOT/%{_bindir}/%{name}

%files
%{_bindir}/%{name}
%doc COPYING README

%changelog
* Tue Aug 07 2012 Wei-Lun Chao <bluebat@member.fsf.org> - 0.2.0
- Rebuilt for Fedora
