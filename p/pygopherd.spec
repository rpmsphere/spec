%define __python /usr/bin/python2

Summary:        Gopher server
Summary(pl):    Serwer gophera
Name:           pygopherd
Version:        2.0.16
Release:        11.1
License:        GPL
Group:          Networking/Daemons
Source0:        https://gopher.quux.org:70/give-me-gopher/pygopherd/%{name}_%{version}.tar.gz
Source1:        %{name}.init
Patch0:         %{name}-conf.patch
URL:            gopher://gopher.quux.org/1/Software/Gopher
Requires(pre):  /usr/bin/id
Requires(pre):  /usr/sbin/groupadd
Requires(pre):  /usr/sbin/useradd
Provides:       gopher-server
Provides:       group(gopher)
Provides:       user(gopher)
Obsoletes:      gofish
Obsoletes:      gopher-server
BuildArch:      noarch
%define         _rootdir        /home/services/gopher
BuildRequires:  python2

%description
gopherd - a gopher server.

%description -l pl
gopherd - serwer gophera.

%prep
%setup -q -n %{name}
%patch 0 -p0

%build
python2 setup.py build

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_sysconfdir}/{%{name},rc.d/init.d},%{python_sitelib},%{_rootdir}}

python2 setup.py install \
        --root=$RPM_BUILD_ROOT \
        --install-lib=%{python_sitelib} \
        --optimize=2

install %{SOURCE1} $RPM_BUILD_ROOT/etc/rc.d/init.d/pygopherd
find $RPM_BUILD_ROOT -type f -name "*.py" -exec rm -rf {} \;

sed -i 's|/usr/bin/python$|/usr/bin/python2|' %{buildroot}%{_bindir}/%{name}

%pre
groupadd -g 30 gopher
useradd -u 13 -g 30 -d /no/home -s /bin/false -c "gopherd user" gopher

%postun
if [ "$1" = "0" ]; then
        userdel gopher
        groupdel gopher
fi

%files
%attr(755,root,root) %{_bindir}/*
%dir %{_sysconfdir}/%{name}
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/%{name}/mime.types
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/%{name}/%{name}.conf
%attr(754,root,root) /etc/rc.d/init.d/pygopherd
%{python_sitelib}/%{name}*

%changelog
* Fri Jun 15 2012 Wei-Lun Chao <bluebat@member.fsf.org> - 2.0.16
- Rebuilt for Fedora
* Fri Sep 08 2006 PLD Team <feedback@pld-linux.org>
All persons listed below can be reached at <cvs_login>@pld-linux.org
$Log: pygopherd.spec,v $
Revision 1.15  2006/09/08 18:03:48  glen
- rel 4 (rebuild with fixed %useradd/%groupadd macros)
Revision 1.14  2006/04/14 15:51:07  glen
- todo is completed, rel 3
Revision 1.13  2005/12/13 14:37:24  glen
- adapterized (sorted %verify flags)
Revision 1.12  2005/05/01 17:31:30  glen
- use %useradd/%groupadd macros
Revision 1.11  2004/12/26 17:27:49  saq
- release 2 for rebuild with python 2.4
Revision 1.10  2004/12/21 00:44:06  undefine
- rel 1
Revision 1.9  2004/10/31 21:05:47  paladine
- spaces->tabs
- formatting
Revision 1.8  2004/09/01 03:29:49  twittner
- exits are back '|| exit 1' -> '|| exit $?' (fixed previous change).
Revision 1.7  2004/08/31 22:33:12  twittner
- don't change return value of (user|group)add if they fail.
Revision 1.6  2004/08/29 16:38:33  zboczuch
- init script
- rel. 5
Revision 1.5  2004/08/29 16:33:03  zboczuch
- root dir
- rel 0.4
Revision 1.4  2004/08/29 16:12:12  zboczuch
- cleanups
- creating group and user, if needed
- rel 0.3
Revision 1.3  2004/08/29 14:37:24  qboosh
- files are not dirs
Revision 1.2  2004/08/29 00:42:33  ankry
- O: gofish, cosmetics, rel. 0.2
Revision 1.1  2004/08/28 22:10:51  undefine
- not tested, just one spec more ;)
