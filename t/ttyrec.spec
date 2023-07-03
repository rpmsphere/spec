Name:               ttyrec
Version:            1.0.8
Release:            10.1
Summary:            Terminal Recorder
Source:             https://0xcc.net/ttyrec/ttyrec-%{version}.tar.gz
Patch1:             ttyrec-terminate_exec_argument_list_with_NULL_instead_of_0.patch
Patch2:             ttyrec-fix_missing_return_in_nonvoid_function.patch
URL:                https://0xcc.net/ttyrec/index.html
Group:              System/Utilities
License:            BSD4c
BuildRequires:      gcc make glibc-devel
Provides:           ttyplay = %{version}
Provides:           ttytime = %{version}

%description
Ttyrec is a tty recorder. It is a derivative of the script command for
recording timing information with microsecond accuracy as well.  It can record
emacs -nw, vi, lynx, or any programs running on tty.

%prep
%setup -q
%patch1
%patch2
sed -i 's|union wait status;|int status;|' ttyrec.c

%build
%__make %{?jobs:-j%{jobs}} \
    CC="%__cc" \
    CFLAGS="%{optflags}"

%install
%__rm -rf "$RPM_BUILD_ROOT"
for f in ttyrec ttyplay ttytime; do
    %__install -D -m0755 "$f" "$RPM_BUILD_ROOT%{_bindir}/$f"
done
for f in *.1; do
    %__install -D -m0644 "$f" "$RPM_BUILD_ROOT%{_mandir}/man1/$f"
done

%clean
%__rm -rf "$RPM_BUILD_ROOT"

%files
%doc README
%{_bindir}/ttyrec
%{_bindir}/ttyplay
%{_bindir}/ttytime
%doc %{_mandir}/man1/ttyrec.1.*
%doc %{_mandir}/man1/ttyplay.1.*
%doc %{_mandir}/man1/ttytime.1.*

%changelog
* Wed Nov 30 2011 Wei-Lun Chao <bluebat@member.fsf.org> - 1.0.8
- Rebuilt for Fedora
* Sun Jun 13 2010 pascal.bleser@opensuse.org
- initial package (1.0.8)
