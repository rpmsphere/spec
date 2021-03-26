Name:           cl-clx
Version:        0.7.4
Release:        4.1
Summary:        Xlib for Common Lisp systems
Group:          System Environment/Libraries
License:        Various (see COPYRIGHT)
URL:            http://common-lisp.net/~abridgewater/
Source:         http://common-lisp.net/~abridgewater/dist/clx/clx-0.7.4.tgz
Source1:        COPYRIGHT
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildRequires:   common-lisp-controller, texinfo
BuildArch:		noarch
Requires:        common-lisp-controller
Requires(post):  common-lisp-controller, /sbin/install-info
Requires(preun): common-lisp-controller, /sbin/install-info

%description
CLX is to Common Lisp as Xlib is to C - it provides an implementation of the X
Window System protocol to Lisp graphics library[ies] and applications.

See McCLIM for the de-facto higher-level toolkit, also see Garnet, CLUE and
CLIO for alternatives.

%prep
%setup -n clx-0.7.4 -q

%build

%install
%{__rm} -rf %{buildroot}

# Replace @NAME@ below with the Common Lisp library name, which may be different from the
# package name if it is not already prefixed with "cl-".

mkdir -m 755 -p %{buildroot}%{_datadir}/common-lisp/source/clx
mkdir -m 755 -p %{buildroot}%{_datadir}/common-lisp/systems

for s in *.lisp; do
  install -m 644 $s %{buildroot}%{_datadir}/common-lisp/source/clx;
done;

mkdir %{buildroot}%{_datadir}/common-lisp/source/clx/{debug,demo,test}

makeinfo manual/clx.texinfo
mkdir -p ${RPM_BUILD_ROOT}%{_infodir}
mv clx.info* ${RPM_BUILD_ROOT}%{_infodir}

for s in *.lisp; do
  install -m 644 $s %{buildroot}%{_datadir}/common-lisp/source/clx;
done;
for dir in demo debug test manual; do
  for s in $dir/* ; do
    install -m 644 $s %{buildroot}%{_datadir}/common-lisp/source/clx/$dir;
  done
done;

for s in *.asd; do
  install -m 644 $s %{buildroot}%{_datadir}/common-lisp/source/clx;
done;
cd %{buildroot}%{_datadir}/common-lisp/source/clx
for asd in *.asd; do
  ln -s %{_datadir}/common-lisp/source/clx/$asd ../../systems;
done

install -m 644 %{SOURCE1} %{buildroot}%{_datadir}/common-lisp/source/clx;

%post
/usr/sbin/register-common-lisp-source clx
/sbin/install-info %{_infodir}/clx.info.gz %{_infodir}/dir || :

%preun
/usr/sbin/unregister-common-lisp-source clx
if [ $1 = 0 ] ; then
    /sbin/install-info --delete %{_infodir}/clx.info %{_infodir}/dir || :
fi

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-,root,root,-)
%doc %{_infodir}/
%{_datadir}/common-lisp/source/clx
%{_datadir}/common-lisp/systems/clx.asd

%changelog
* Thu Feb 28 2013 Wei-Lun Chao <bluebat@member.fsf.org> - 0.7.4
- Rebuild for Fedora
* Mon Apr 4 2011 Wesley Dawson - 0.9.7
- Build requires makeinfo and install-info
* Sun Apr 3 2011 Wesley Dawson - 0.7.4
- Initial build.
