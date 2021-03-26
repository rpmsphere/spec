Name:           prll
Summary:        Easily execute stuff in parallel
License:        GPL v3 or later
Group:          System/Shells
Version:        0.6.2
Release:        3.1
URL:            http://prll.sourceforge.net/
Requires:       grep
BuildRequires:  make
BuildRequires:  gcc
BuildRequires:  bash
BuildRequires:  zsh
BuildRequires:  coreutils
BuildRequires:  grep
Source0:        http://sourceforge.net/projects/prll/files/%{name}-%{version}.tar.bz2
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
While every full-featured shell provides job control, it is only meant for
manual, interactive handling of several jobs, and not much more. prll
(pronounced "parallel") was created to simplify a common task of running a
large number of jobs a few at a time. 

If you have a bunch of files to process, a loop is what you need. However, if
you have a multicore/multiprocessor machine, it is much more efficient to run
as many processes in parallel as there are CPUs available. While a minor
extension to the loop might be adequate, it is not the most efficient solution.

prll is implemented as a shell function, with helper programs written in C.
While there are other ways to tackle the problem, like using the xargs utility,
and while many are "saner" in some sense, having a shell function has a
distinct advantage: you don't need to write any scripts or programs. Implement
your task as a shell function, and prll will run it using the context of your
current shell. 

Summary of features:
* Easy to use. Focuses on a single task and doesn't try to emulate a kitchen sink.
* Code is passed in shell functions to ease interactive use.
* Works in both bash and zsh and in several operating systems.
* Execution can be terminated gracefully, letting started jobs finish their work.
* Can be terminated from within the code it executes, easing aborting on errors or 
  implementing an ad-hoc parallel search.
* Does internal buffering and locking to prevent mangling/interleaving of output 
  from separate jobs.

Author:
--------
    Jure Varlec

%prep
%setup -q 

%build
export CFLAGS="%optflags" 
make %{?jobs:-j%jobs}

%install
mkdir -p %buildroot/%_bindir
for file in prll_qer prll_bfr; do
    install -m755 $file %buildroot/%_bindir/
done
echo "#!/bin/sh" > %buildroot/%_bindir/prll
cat prll.sh >> %buildroot/%_bindir/prll
chmod +x %buildroot/%_bindir/prll
mkdir -p %buildroot/%_datadir/%name
install -m644 prll.sh %buildroot/%_datadir/%name/prll.sh
# install completions
for dir in profile.d bash_completion.d ; do
	mkdir -p %buildroot/%_sysconfdir/$dir
	cat >> %buildroot/%_sysconfdir/$dir/%name << EOF
source %_datadir/%name/prll.sh
EOF
done

%clean
rm -rf ${RPM_BUILD_ROOT}

%files
%defattr(-,root,root)
%doc AUTHORS COPYING NEWS README 
%_bindir/*
%_datadir/%name
%config(noreplace) %_sysconfdir/bash_completion.d/%name
%config(noreplace) %_sysconfdir/profile.d/%name

%changelog
* Wed Sep 25 2013 Wei-Lun Chao <bluebat@member.fsf.org> - 0.6.2
- Rebuild for Fedora
* Tue Jun 22 2010 lars@linux-schulserver.de
- use group System/Shells
* Sat May  1 2010 lars@linux-schulserver.de
- install profile.d and back-completion.d files
* Sat May  1 2010 lars@linux-schulserver.de
- initial version 0.5
