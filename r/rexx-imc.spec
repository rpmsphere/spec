%undefine _debugsource_packages

Summary: IMC's interpreter for the Rexx
Name: rexx-imc
Version: 1.76
Release: 5.1
License: distributable
Group: Development/Languages
URL: http://www.cs.ox.ac.uk/people/ian.collier/Rexx/rexximc.html
Source: %{name}-1.7.tar.gz
Patch0: rexx-imc-1.7-1.75.patch
Patch1: rexx-imc-1.75-1.76.patch
Conflicts: regina

%description
Rexx is a procedural programming language that allows programs
and algorithms to be written in a clear and structured way, and
it is designed to be easy to use as well as flexible.  It can
also easily be embedded into an application to make it scriptable.

%prep
%setup -q -n %{name}-1.7
%patch0 -p1
%patch1 -p1

%build
./Make PREFIX=/usr REXXLIB=/usr/lib/rexx

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/usr/{lib/rexx,bin,man/man1,include}
./Make PREFIX=$RPM_BUILD_ROOT/usr REXXLIB=$RPM_BUILD_ROOT/usr/lib/rexx RUNLIBS= install
cp -p rexxsaa.h $RPM_BUILD_ROOT/usr/include

%clean
rm -rf $RPM_BUILD_ROOT

%files
%doc README* rexx.info rexx.ref rexx.summary rexx.tech
/usr/bin/*
/usr/lib/*
/usr/man/man1/*
/usr/include/rexxsaa.h

%changelog
* Sun Oct 21 2012 Wei-Lun Chao <bluebat@member.fsf.org> - 1.76
- Rebuilt for Fedora
* Tue Feb 26 2002 Ian Collier <imc@comlab.ox.ac.uk>
- Initial package
