Name:         imap2mbox
Summary:      IMAP Folder to MBOX Mailbox Transfer
URL:          http://www.zerozone.it/Software/Linux/imap2mbox/
Group:        Mail
License:      LGPL
Version:      1.5.0
Release:      3.1
Source0:      http://www.zerozone.it/Software/Linux/imap2mbox/imap2mbox-%{version}.tar.gz
BuildArch:    noarch

%description
IMAP2MBOX transfers mails from a remote IMAP folder to a local MBOX
format mailbox.

%prep
%setup -q -n imap2mbox

%build

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p -m 755 \
    $RPM_BUILD_ROOT%{_bindir} \
    $RPM_BUILD_ROOT%{_libexecdir}/imap2mbox
install -c -m 755 \
    imap2mbox.py $RPM_BUILD_ROOT%{_libexecdir}/imap2mbox/
cp -rp \
    imap2mbox $RPM_BUILD_ROOT%{_libexecdir}/imap2mbox/
( echo "#!/bin/sh"
  echo "PYTHONPATH=%{_libexecdir}/imap2mbox:\$PYTHONPATH"
  echo "export PYTHONPATH"
  echo "exec python \\"
  echo "    %{_libexecdir}/imap2mbox/imap2mbox.py \\"
  echo "    \${1+\"\$@\"}"
) >imap2mbox.sh
install -c -m 755 \
    imap2mbox.sh $RPM_BUILD_ROOT%{_bindir}/imap2mbox

sed -i 's|/usr/bin/env python$|/usr/bin/python2|' %{buildroot}%{_libexecdir}/%{name}/%{name}.py

%files
%{_bindir}/%{name}
%{_libexecdir}/%{name}

%clean
rm -rf $RPM_BUILD_ROOT

%changelog
* Wed Sep 25 2013 Wei-Lun Chao <bluebat@member.fsf.org> - 1.5.0
- Rebuild for Fedora
