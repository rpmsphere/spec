%undefine _debugsource_packages

Name:         heirloom-sh
Summary:      Traditional Bourne-Shell
URL:          https://heirloom.sourceforge.net/sh.html
Group:        Shell
License:      BSD/CDDL
Version:      050706
Release:      6.1
Source0:      https://switch.dl.sourceforge.net/sourceforge/heirloom/heirloom-sh-%{version}.tar.bz2
Patch:       sh.patch

%description
The Heirloom Bourne Shell is a portable variant of the traditional
Unix Bourne shell. It has been derived from OpenSolaris code and
thus implements the SVR4/SVID3 level of the shell. Although the
Bourne shell is not POSIX-conforming because the POSIX.2 standard
introduced requirements for the shell that were incompatible with
existing Bourne shell behavior, it remains the father of all Unix
shell scripting languages. Most scripts that run in the Heirloom
Bourne Shell will run with any Unix shell that is still in use in
the twenty-first century.

%prep
%setup -q
%patch -p0

%build
%{__make} %{_smp_mflags} \
    CC="%{__cc}" \
    CFLAGS="%{optflags -O}" \
    PREFIX=%{_prefix} \
    SV3BIN=%{_bindir} \
    MANDIR=%{_mandir}

%install
%{__make} %{_smp_mflags} install \
    ROOT=$RPM_BUILD_ROOT \
    PREFIX=%{_prefix} \
    SV3BIN=%{_bindir} \
    MANDIR=%{_mandir} \
    UCBINST="install -c" \
    LNS="ln"

rm %{buildroot}%{_bindir}/jsh %{buildroot}%{_mandir}/man1/jsh.*
mv %{buildroot}%{_bindir}/sh %{buildroot}%{_bindir}/%{name}
mv %{buildroot}%{_mandir}/man1/sh.1 %{buildroot}%{_mandir}/man1/%{name}.1

%files
%{_bindir}/%{name}
%{_mandir}/man1/%{name}.1.*

%changelog
* Wed Sep 25 2013 Wei-Lun Chao <bluebat@member.fsf.org> - 050706
- Rebuilt for Fedora
