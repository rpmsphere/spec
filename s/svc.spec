Name:      svc
Version:   200601111324
Release:   3.1
Group:     System/Base
License:   GPL
URL:       https://gpl.internetconnection.net/
Source:    https://gpl.internetconnection.net/files/svc.tar.gz
Patch0:     svc_build.patch
Summary:   Service toolbox

%description
Service toolbox for building trigger-launched programs, wrapping TTYs, and
making lockfiles.

%prep
%setup -n %{name}
%patch 0

%build
# -lutil for forkpty
CFLAGS="%{optflags} -DUSE_FCNTL -DUSE_FORKPTY" \
LDFLAGS="-lutil" \
%{__make}

%install
%{__rm} -rf $RPM_BUILD_ROOT
for i in lockf  pull-trigger  sleep-svc  ttywrap  wait-trigger ; do
    %{__install} -D -m 0755 $i $RPM_BUILD_ROOT%{_sbindir}/$i
done

%files
%{_sbindir}/lockf
%{_sbindir}/pull-trigger
%{_sbindir}/sleep-svc
%{_sbindir}/ttywrap
%{_sbindir}/wait-trigger
%doc CHANGELOG

%changelog
* Tue Aug 21 2012 Wei-Lun Chao <bluebat@member.fsf.org> - 200601111324
- Rebuilt for Fedora
* Sat Oct  7 2006 mrueckert@suse.de
- initial package
