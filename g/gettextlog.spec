%undefine _debugsource_packages

Summary:   Simple preloadable shared library to log untranslated messages
Name:      gettextlog
Version:   0.6
Release:   4.1
License:   LGPL
URL:       https://sourceforge.net/projects/gettextlog/
Source:    https://downloads.sourceforge.net/project/gettextlog/gettextlog/%{name}-%{version}/%{name}-%{version}.tar.gz
Group:     Development/Tools

%prep
%setup -q
sed -i 's/-Wall/-fPIC -Wall/' Makefile

%build
make all

%install
make PREFIX=$RPM_BUILD_ROOT%{_prefix} install

%description
Gettextlog intercepts calls to gettext and log all untranslated (or just all)
messages to log file. Useful for translators of big programs, because
they can separate more frequent and less frequent messages and
translate more frequent first.
 
%files
%doc README COPYING
%{_prefix}/lib/gettextlog.so
%{_prefix}/bin/run-with-gettextlog

%clean
rm -rf $RPM_BUILD_ROOT

%changelog
* Sun Apr 24 2011 Wei-Lun Chao <bluebat@member.fsf.org> - 0.6
- Rebuilt for Fedora
