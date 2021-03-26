Name: launchtool
Version: 0.8
Release: 6.1
Summary: Runs a command supervising its execution
License: GPLv2+
Group: System/Base
URL: http://people.debian.org/~enrico/launchtool.html
Source: %{name}-%{version}.tar.gz
Patch1: launchtool-0.7-pidfile.patch
BuildRequires: popt-devel

%description
launchtool is a tool that runs a user-supplied command and can supervise its
execution in many ways, such as controlling its environment, blocking signals,
logging its output, changing user and group permissions, limiting resource
usage, restarting it if it fails, running it continuously and turn it into a
daemon.

%prep
%setup -q
%patch1 -p1

%build
%configure --localstatedir=/var
make

%install
%make_install install DESTDIR=%buildroot
install -pD -m644 launchtool.1 %buildroot%_man1dir/launchtool.1

%files
%_bindir/*
%_mandir/man1/*

%changelog
* Wed Feb 18 2015 Wei-Lun Chao <bluebat@member.fsf.org> - 0.8
- Rebuild for Fedora
* Mon Apr 15 2013 Dmitry V. Levin (QA) <qa_ldv@altlinux.org> 0.7-alt1.qa1
- NMU: rebuilt for debuginfo.
* Mon Jan 05 2009 Victor Forsyuk <force@altlinux.org> 0.7-alt1
- Initial build.
