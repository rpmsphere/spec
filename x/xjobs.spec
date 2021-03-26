Name:         xjobs
Summary:      Parallel Execution of Jobs
URL:          http://www.maier-komor.de/xjobs.html
Group:        ShellUtils
License:      GPL
Version:      20120412
Release:      7.1
Source0:      http://www.maier-komor.de/xjobs/xjobs-%{version}.tgz
Patch:        xjobs.patch

%description
xjobs reads job descriptions line by line and executes them in
parallel. It limits the number of parallel executing jobs and starts
new jobs when jobs finish. Therefore, it combines the arguments from
every input line with the utility and arguments given on the command
line. If no utility is given as an argument to xjobs, then the first
argument on every job line will be used as utility. To execute
utility xjobs searches the directories given in the PATH environment
variable and uses the first file found in these directories. xjobs
is most useful on multiprocessor machines when one needs to execute
several time consuming command several that could possibly be run in
parallel. With xjobs this can be achieved easily, and it is possible
to limit the load of the machine to a useful value. It works similar
to xargs, but starts several processes simultaneously and gives only
one line of arguments to each utility call.

%prep
%setup -q
%patch -p0

%build
./configure \
    --prefix=%{_prefix} \
    --build=x86_64 \
    --mandir=%{_mandir}
%{__make} %{_smp_mflags -O}

%install
%{__make} %{_smp_mflags} install \
    prefix=$RPM_BUILD_ROOT%{_prefix} \
    exec_prefix=$RPM_BUILD_ROOT%{_prefix} \
    mandir=$RPM_BUILD_ROOT%{_mandir}/man1

%files
%{_bindir}/*
%{_mandir}/man1/*

%changelog
* Wed Sep 25 2013 Wei-Lun Chao <bluebat@member.fsf.org> - 20120412
- Rebuild for Fedora
