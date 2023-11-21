%undefine _auto_set_build_flags

Name: taskspooler
Summary: Personal job scheduler
Version: 0.7.5
Release: 4.1
Group: Applications/Productivity
License: GPLv2
URL: https://vicerveza.homeunix.net/~viric/soft/ts/
Source0: https://vicerveza.homeunix.net/~viric/soft/ts/ts-%{version}.tar.gz

%description
Task spooler is a Unix batch system where the tasks spooled run one
after the other. Each user in each system has his own job queue. The tasks are
run in the correct context (that of enqueue) from any shell/process, and its
output/results can be easily watched. It is very useful when you know that
your commands depend on a lot of RAM, a lot of disk use, give a lot of
output, or for whatever reason it's better not to run them at the same time.

%prep
%setup -q -n ts-%{version}

%build
make %{?_smp_mflags}

%install
install -Dm755 ts %{buildroot}%{_bindir}/%{name}
install -Dm644 ts.1 %{buildroot}%{_mandir}/man1/%{name}.1

%files
%doc Changelog COPYING README TRICKS PROTOCOL
%{_bindir}/%{name}
%{_mandir}/man1/%{name}.1.*

%changelog
* Thu Jun 04 2015 Wei-Lun Chao <bluebat@member.fsf.org> - 0.7.5
- Rebuilt for Fedora
