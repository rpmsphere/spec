Name:         tsp
Summary:      Task Spooler
URL:          http://vicerveza.homeunix.net/~viric/soft/ts/
Group:        ShellUtils
License:      GPL
Version:      0.7.3
Release:      4.1
Source0:      http://vicerveza.homeunix.net/~viric/soft/ts/ts-%{version}.tar.gz

%description
Task Spooler is a Unix batch system where the tasks spooled run
one after the other. The amount of jobs to run at once can be set
at any time. Each user in each system has his own job queue. The
tasks are run in the correct context from any shell/process, and its
output/results can be easily watched. It is very useful when you
know that your commands depend on a lot of RAM, a lot of disk use,
give a lot of output, or for whatever reason it's better not to run
them all at the same time, while you want to keep your resources
busy for maximum benfit. Its interface allows using it easily in
scripts.

%prep
%setup -q -n ts-%{version}

%build
%{__make} %{_smp_mflags -O} \
    GLIBCFLAGS="-D_XOPEN_SOURCE=500 -D__STRICT_ANSI__"

%install
mkdir -p -m 755 \
    $RPM_BUILD_ROOT%{_bindir} \
    $RPM_BUILD_ROOT%{_mandir}/man1
install -c -m 755 \
    ts $RPM_BUILD_ROOT%{_bindir}/tsp
install -c -m 644 \
    ts.1 $RPM_BUILD_ROOT%{_mandir}/man1/tsp.1

%files
%{_bindir}/tsp
%{_mandir}/man1/tsp.1.*

%changelog
* Wed Sep 25 2013 Wei-Lun Chao <bluebat@member.fsf.org> - 0.7.3
- Rebuilt for Fedora
