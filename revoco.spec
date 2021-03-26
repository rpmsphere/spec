Name:				revoco
Version:			0.4
Release:			3.1
Summary:			Wheel Behaviour Configuration Tool for the Logitech MX-Revolution Mouse
Source:			http://goron.de/~froese/revoco/revoco-%{version}.tar.gz
Patch1:			revoco-fix_makefile_flags.patch
URL:				http://goron.de/~froese/revoco/
Group:			Hardware/Other
License:			Public Domain
BuildRoot:		%{_tmppath}/build-%{name}-%{version}
BuildRequires:	gcc make glibc-devel
BuildRequires:	help2man

%description
Change the wheel behaviour of Logitech's MX-Revolution mouse.

Authors:
--------
    Edgar Toernig <froese@gmx.de>

%prep
%setup -q
%patch1

%build
%__make %{?jobs:-j%{jobs}} \
		  CC="%__cc" \
		  OPTFLAGS="%{optflags}"

help2man \
			--version-option='-h|echo %{version}' \
			--no-info \
			--section=8 \
			--name='%{name}' \
			--output='%{name}.8' \
			./revoco

%install
%__rm -rf "$RPM_BUILD_ROOT"
%__install -D -m0755 revoco "$RPM_BUILD_ROOT%{_bindir}/revoco"
%__install -D -m0644 revoco.8 "$RPM_BUILD_ROOT%{_mandir}/man8/revoco.8"

%clean
%__rm -rf "$RPM_BUILD_ROOT"

%files
%defattr(-,root,root)
%{_bindir}/revoco
%doc %{_mandir}/man8/revoco.8*

%changelog
* Wed Nov 30 2011 Wei-Lun Chao <bluebat@member.fsf.org> - 0.4
- Rebuild for Fedora

* Sun Dec 30 2007 Pascal Bleser <guru@unixtech.be> 0.4
- new package

# Local Variables:
# mode: rpm-spec
# tab-width: 3
# End:
