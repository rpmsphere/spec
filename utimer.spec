Name:           utimer
Version:        0.4
Release:        2.1
Summary:        Command-line multifunction timer tool
License:        GPLv3+
URL:            http://utimer.codealpha.net/utimer/
Source0:        http://utimer.codealpha.net/files/%{name}-%{version}.tar.gz
BuildRequires: intltool, glib2-devel

%description 
utimer is a command-line multifunction timer tool.
It features a timer, a countdown, and a stopwatch.

%prep
%setup -q

%build
export LDFLAGS=-Wl,--allow-multiple-definition
%configure
make %{?_smp_mflags}

%install
make DESTDIR=%{buildroot} install

%files 
%doc AUTHORS ChangeLog COPYING README 
%{_mandir}/man1/%{name}.1.gz
%{_bindir}/%{name}

%changelog
* Sun Jun 23 2013 Wei-Lun Chao <bluebat@member.fsf.org> - 0.4
- Rebuild for Fedora
* Sun Jul 01 2012 Simone Sclavi <darkhado@gmail.com> 0.4-1
- Initial build
