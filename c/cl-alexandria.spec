Name:           cl-alexandria
Version:        20181203git
Release:        1
Summary:        Collection of portable Common Lisp utilities
Group:          System Environment/Libraries
License:        Public Domain
URL:            https://common-lisp.net/project/alexandria/
# git clone https://gitlab.common-lisp.net/alexandria/alexandria.git
Source:         alexandria-master.zip
BuildRequires:  common-lisp-controller
BuildArch:	noarch
Requires:       common-lisp-controller

%description
Alexandria is a collection of utilities in the public domain for Common Lisp.
It is a library but also a project that aims to reduce duplication of effort
and improve portability of Common Lisp code according to its own idiosyncratic
and rather conservative aesthetic.
It is used by other projects as a base to build on.

%prep
%setup -q -n alexandria-master

%build

%install
%{__rm} -rf %{buildroot}

# Replace @NAME@ below with the Common Lisp library name, which may be different from the
# package name if it is not already prefixed with "cl-".

mkdir -m 755 -p %{buildroot}%{_datadir}/common-lisp/source/cl-alexandria
mkdir -m 755 -p %{buildroot}%{_datadir}/common-lisp/systems

for s in *.lisp; do
  install -m 644 $s %{buildroot}%{_datadir}/common-lisp/source/cl-alexandria;
done;

for s in *.asd; do
  install -m 644 $s %{buildroot}%{_datadir}/common-lisp/source/cl-alexandria;
done;
cd %{buildroot}%{_datadir}/common-lisp/source/cl-alexandria
for asd in *.asd; do
  ln -s %{_datadir}/common-lisp/source/cl-alexandria/$asd ../../systems;
done

%post
/usr/sbin/register-common-lisp-source cl-alexandria

%preun
/usr/sbin/unregister-common-lisp-source cl-alexandria

%clean
%{__rm} -rf %{buildroot}

%files
%doc README LICENCE AUTHORS
%{_datadir}/common-lisp/source/cl-alexandria
%{_datadir}/common-lisp/systems/*.asd

%changelog
* Mon Dec 23 2019 Wei-Lun Chao <bluebat@member.fsf.org> - 20181203git
- Rebuilt for Fedora
