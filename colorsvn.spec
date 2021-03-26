Name:           colorsvn
Version:        0.3.2
Release:        3.1
Summary:        Colorizer for SVN, based on colorgcc
Group:          Development/Tools/Version Control
License:        GPL
URL:            http://www.console-colors.de/
Source0:        %{name}-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root
BuildRequires:  subversion
Requires:       subversion 
BuildArch:      noarch

%description
colorsvn will execute subversion commands and colorize the output.

%prep
%setup -q

%build
%configure 

%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%config(noreplace) %{_sysconfdir}/colorsvnrc
%doc CREDITS
%{_mandir}/man1/colorsvn.1.*
%{_bindir}/colorsvn
%config(noreplace) %{_sysconfdir}/profile.d/colorsvn-env.sh

%changelog
* Wed Sep 25 2013 Wei-Lun Chao <bluebat@member.fsf.org> - 0.3.2
- Rebuild for Fedora
* Sat Mar 24 2012 toms@opensuse.org
- Initial version 0.3.2
