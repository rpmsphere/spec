Name:     log4sh
Summary:  Advanced Logging Framework for Shell Scripts
Version:  1.4.2
Release:  6.1
Source0:  %{name}-%{version}.tgz
Patch0:   %{name}-docbook-src.diff
License:  LGPL-2.1
Group:    Development/Languages/Other
URL:      https://sourceforge.net/projects/log4sh/
BuildArch: noarch
BuildRequires: bash
BuildRequires: libxml2
BuildRequires: libxslt
BuildRequires: docbook-style-xsl

%description
log4sh is an advanced logging framework for shell scripts (eg. sh, bash) 
that works similar to the logging products available from the 
Apache Software Foundataion (eg. log4j, log4perl).

%prep
%setup -q
%patch 0 -p1

%build

%install
mkdir -p $RPM_BUILD_ROOT%{_datadir}/%{name}
install src/shell/log4sh $RPM_BUILD_ROOT%{_datadir}/%{name}

%files 
%doc doc/log4sh.html doc/style.css doc/*.txt doc/LGPL-2.1
%{_datadir}/%{name}

%changelog
* Wed Sep 25 2013 Wei-Lun Chao <bluebat@member.fsf.org> - 1.4.2
- Rebuilt for Fedora
* Mon Mar 19 2012 toms@opensuse.org
- First release 1.4.2
