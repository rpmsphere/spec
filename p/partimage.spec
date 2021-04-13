Summary: 	Partition Image
Name: 		partimage
Version: 	0.6.9
Release: 	15
URL: 		http://www.partimage.org/
License: 	GPLv2
Group: 		Archiving/Backup
Source: 	%{name}-%{version}.tar.bz2
Source1:	partimage.1
Source2:	partimaged.8
Source3:	partimagedusers.5
Source4:	partimaged-sysconfig
Source5:	partimaged-init.d
Patch3: 	partimage-0.6.7-ssl-certs-policy.patch
Patch12:	partimage-0.6.8-lzma.patch
Patch13:	partimage-0.6.7-splash.patch
Patch14:	partimage-0.6.9-fedora-gzfile.patch
Patch15:	partimage-0.6.9-automake-1.13.patch
Patch16:	partimage-0.6.9-no-sslv2.patch
# from debian: fix build config with openssl 1.1
Patch17:	03-openssl11.patch
Patch18:	partimage-0.6.9-sysmacros.patch
BuildRequires:	bzip2-devel
BuildRequires:	gettext-devel
#BuildRequires:	lzmadec-devel
BuildRequires:	pkgconfig(libnewt)
BuildRequires:	pkgconfig(openssl)
BuildRequires:	pkgconfig(zlib)

%description
Partition Image is a Linux/UNIX partition imaging utility: it saves
partitions in the following file system formats to an image file:
- Ext2FS & Ext3FS (the Linux standard),
- FAT16/32 (DOS & Windows file systems),
- HFS (MacOS File System),
- JFS (Journalised File System, from IBM, used on AIX),
- NTFS (Windows NT File System),
- HPFS (IBM OS/2 File System),
- ReiserFS (a journalized and powerful file system),
- UFS (Unix File System),
- XFS (another journalized and efficient File System, from SGI, used on Irix),

Only used blocks are copied. The image file can be
compressed into the GZIP/BZIP2 formats to save disk space, and split
into multiple files to be copied onto floppies (ZIP for example),
or burned on a CD-R ...

This allows saving a full Linux/Windows system, with only one
operation. When problems (viruses, crash, error, ...) occur, you just have to
restore, and after several minutes, all your system is restored (boot,
files, ...), and fully working.

This is very useful when installing the same software on many
machines: just install one of them, create an image, and just restore
the image on all other machines. Then, after the first one, each
installation is automatically made, and only requires a few minutes.

%prep
%autosetup -p1

%build
autoreconf -vfi
%configure
%make_build

%install
%make_install
rm -rf %{buildroot}%{_infodir}/*
install -m644 %{SOURCE1} -D %{buildroot}%{_mandir}/man1/partimage.1
install -m644 %{SOURCE2} -D %{buildroot}%{_mandir}/man8/partimaged.8
install -m644 %{SOURCE3} -D %{buildroot}%{_mandir}/man5/partimagedusers.5
install -m644 %{SOURCE4} -D %{buildroot}%{_sysconfdir}/sysconfig/partimaged
install -m755 %{SOURCE5} -D %{buildroot}%{_initrddir}/partimaged

cat > README.mga <<EOF
Mageia RPM specific notes

setup
-----
In order to comply with Mageia SSL certificates policy, partimage binary has
been modified to use the following files:
- /etc/pki/tls/certs/partimage.pem instead of default
  /etc/partimaged/partimaged.cert
- /etc/pki/tls/private/partimage.pem instead of default
  /etc/partimaged/partimaged.key
EOF

%find_lang %{name}

sed -i 's|gprintf|printf|' %{buildroot}%{_initrddir}/partimaged

%pre
groupadd -r partimag ||:
useradd partimag -g partimag -d /var/lib/partimage -r -s /bin/false

%post
dir=/var/lib/partimage
if [ ! -d $dir ]; then
    mkdir -p $dir/{dev,etc,%{_lib},var/log}
    cp -a /dev/{null,tty} $dir/dev
    cp /%{_lib}/{libnss_compat.so.2,libnss_files.so.2} $dir/%{_lib}
    grep partimag /etc/passwd > $dir/etc/passwd
    grep partimag /etc/group > $dir/etc/group
    install -d -o partimag $dir/data
fi
#%_create_ssl_certificate partimage -g partimag
mkdir -p /etc/pki/tls/certs/ /etc/pki/tls/private/
openssl req -newkey rsa:4096 \
            -x509 \
            -sha256 \
            -days 3650 \
            -nodes \
            -out /etc/pki/tls/certs/partimage.pem \
            -keyout /etc/pki/tls/private/partimage.pem \
            -subj "/C=SI/ST=Ljubljana/L=Ljubljana/O=Security/OU=IT Department/CN=www.example.com"
# now all you have to do is run partimaged -D --chroot /var/lib/partimage
service partimaged start

%preun
service partimaged stop

%postun
userdel partimag
groupdel partimag ||:

%files -f %{name}.lang
%doc BUGS AUTHORS ABOUT-NLS COPYING ChangeLog partimage.lsm
%doc FORMAT README README.partimaged README.mga THANKS
%{_sbindir}/*
%{_sysconfdir}/sysconfig/partimaged
%{_initrddir}/partimaged
%attr(0600,partimag,partimag) %config(noreplace) %{_sysconfdir}/partimaged/partimagedusers
%{_mandir}/man1/partimage.1*
%{_mandir}/man5/partimagedusers.5*
%{_mandir}/man8/partimaged.8*

%changelog
* Mon Mar 15 2021 Wei-Lun Chao <bluebat@member.fsf.org> - 0.6.9
- Rebuild for Fedora

* Tue Jan 19 2021 luigiwalser <luigiwalser> 0.6.9-15.mga8
+ Revision: 1672508
- use standard Mageia macro for creating partimag user

* Fri Feb 14 2020 umeabot <umeabot> 0.6.9-14.mga8
+ Revision: 1520139
- Mageia 8 Mass Rebuild
+ wally <wally>
- replace deprecated %%configure2_5x

* Mon Nov 05 2018 umeabot <umeabot> 0.6.9-13.mga7
+ Revision: 1328455
- Mageia 7 Mass Rebuild

* Wed Sep 06 2017 cjw <cjw> 0.6.9-12.mga7
+ Revision: 1151704
- rebuild with openssl 1.1

* Thu Sep 01 2016 daviddavid <daviddavid> 0.6.9-11.mga6
+ Revision: 1049700
- replace BR liblzmadec-devel to lzmadec-devel

* Thu Mar 03 2016 daviddavid <daviddavid> 0.6.9-10.mga6
+ Revision: 984093
- add patch16 to fix build with openssl with sslv2 disabled
+ umeabot <umeabot>
- Rebuild for openssl

* Fri Feb 12 2016 umeabot <umeabot> 0.6.9-9.mga6
+ Revision: 956627
- Mageia 6 Mass Rebuild

* Mon Oct 19 2015 danf <danf> 0.6.9-8.mga6
+ Revision: 892783
- Fixed packaging with new rpm %%doc behaviour
- Fixed some typos in the description
- Changed some BuildRequires to use pkgconfig() syntax

* Wed Oct 15 2014 umeabot <umeabot> 0.6.9-7.mga5
+ Revision: 741942
- Second Mageia 5 Mass Rebuild

* Tue Sep 16 2014 umeabot <umeabot> 0.6.9-6.mga5
+ Revision: 683345
- Mageia 5 Mass Rebuild

* Fri Oct 18 2013 umeabot <umeabot> 0.6.9-5.mga4
+ Revision: 508907
- Mageia 4 Mass Rebuild

* Sun Jan 13 2013 umeabot <umeabot> 0.6.9-4.mga3
+ Revision: 362432
- Mass Rebuild - https://wiki.mageia.org/en/Feature:Mageia3MassRebuild

* Wed Jan 09 2013 zezinho <zezinho> 0.6.9-3.mga3
+ Revision: 344158
- add patch for automake-1.13

* Wed Jan 09 2013 zezinho <zezinho> 0.6.9-2.mga3
+ Revision: 344139
- patch from fedora to fix build against zlib >= 1.2.6

* Sat Apr 16 2011 pterjan <pterjan> 0.6.9-1.mga1
+ Revision: 86567
- Update to 0.6.9

* Thu Feb 24 2011 ennael <ennael> 0.6.8-4.mga1
+ Revision: 58812
- clean spec
- imported package partimage


* Fri Dec 03 2010 Oden Eriksson <oeriksson@mandriva.com> 0.6.8-4mdv2011.0
+ Revision: 607073
- rebuild

* Wed Apr 07 2010 Funda Wang <fwang@mandriva.org> 0.6.8-3mdv2010.1
+ Revision: 532519
- add fedora patch to build with openssl 1.0

* Fri Feb 26 2010 Oden Eriksson <oeriksson@mandriva.com> 0.6.8-2mdv2010.1
+ Revision: 511611
- rebuilt against openssl-0.9.8m

* Sat Sep 26 2009 Frederik Himpe <fhimpe@mandriva.org> 0.6.8-1mdv2010.0
+ Revision: 449320
- Fix BuildRequires for lzma support
- Update to new version 0.6.8
- Remove patches integrated upstream (nologin, inttypes, setegid,
  set-effective-gid, save_file_and_rest_file_actions, nossl, gcc43)
- Remove slang patch: not needed because it uses -I/usr/include/slang
- Remove disable_header_check Debian patch: not needed since 0.6.5
  according to Debian changelog
- Rediff lzma patch
- Add patch fixing build with -Werror=format-security

* Wed Nov 05 2008 Olivier Blin <oblin@mandriva.com> 0.6.7-12mdv2009.1
+ Revision: 300043
- fix crash in restore when bootsplash is disabled in kernel

* Thu Sep 04 2008 Olivier Blin <oblin@mandriva.com> 0.6.7-11mdv2009.0
+ Revision: 280712
- create /etc/group in jail
- fix setting group when dropping privileges (#42890)

* Fri Jun 13 2008 Olivier Blin <oblin@mandriva.com> 0.6.7-9mdv2009.0
+ Revision: 218815
- do not use jail by default (make it configurable in /etc/sysconfig/partimaged)
- run partimaged in jail without login and ssl support

* Thu Jun 12 2008 Olivier Blin <oblin@mandriva.com> 0.6.7-8mdv2009.0
+ Revision: 218372
- bump release
- update bootsplash support from Brazilian OEM package (salem/claudio/ehabkost ?)
- initial bootsplash support from Brazilian OEM package (salem/claudio/ehabkost ?)
- lzma support from Brazilian OEM package (salem/claudio/ehabkost ?)
- make sure inttypes.h is included early (so that other headers like lzmadec.h do not include it in a wrong way)

* Wed Jun 11 2008 Guillaume Rousse <guillomovitch@mandriva.org> 0.6.7-7mdv2009.0
+ Revision: 217867
- add README.mdv with mandriva-specific SSL certs note

* Tue Jun 10 2008 Olivier Blin <oblin@mandriva.com> 0.6.7-6mdv2009.0
+ Revision: 217690
- remove support of "--with jail" (last pixelware bits)
- always create jail and install initscript
- always create certificates
- always install partimagedusers
- do not disable login and ssl support when building jail, this can now be disabled at runtime
- always apply save/rest_file patch
- allow --nologin for client (even if built with login support)
- allow --nossl for server (even if built with ssl support)
- do not redefine write_unsigned and read_unsigned in save/rest_file patch

* Mon Jun 09 2008 Thierry Vignaud <tv@mandriva.org> 0.6.7-5mdv2009.0
+ Revision: 217015
- other file systems are supported
- add missing colon
- reorder FSes (silent)
- fix description

* Fri Jun 06 2008 Pixel <pixel@mandriva.com> 0.6.7-4mdv2009.0
+ Revision: 216456
- fix build with gcc 4.3

* Wed May 07 2008 Guillaume Rousse <guillomovitch@mandriva.org> 0.6.7-3mdv2009.0
+ Revision: 202834
- patch4: set effective gid as well as effective uid, to be able to use group perms

* Wed Mar 05 2008 Guillaume Rousse <guillomovitch@mandriva.org> 0.6.7-2mdv2008.1
+ Revision: 180009
- ssl certs policy compliance

* Mon Feb 04 2008 Frederik Himpe <fhimpe@mandriva.org> 0.6.7-1mdv2008.1
+ Revision: 162508
- New upstream version
- Remove patch 6,7: integrated upstream
- Rediff patch 1
- Add LSB headers to partimaged init script (copied from Debian)

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Thu Jul 26 2007 Herton Ronaldo Krzesinski <herton@mandriva.com.br> 0.6.5-5mdv2008.0
+ Revision: 56115
- Added workaround from debian to allow partimage run on x86_64
  (partimage-0.6.5-deb_disable_header_check.patch). Closes: #20740

* Thu May 31 2007 Herton Ronaldo Krzesinski <herton@mandriva.com.br> 0.6.5-4mdv2008.0
+ Revision: 33397
- Rebuild again, for rpm changelog fix.

* Thu May 31 2007 Herton Ronaldo Krzesinski <herton@mandriva.com.br> 0.6.5-3mdv2008.0
+ Revision: 33309
- Rebuild with libnewt0.52.


* Tue Mar 06 2007 Pixel <pixel@mandriva.com> 0.6.5-2mdv2007.0
+ Revision: 133763
- add autoreconf (as explained by Olivier Lahaye)

* Tue Mar 06 2007 Pixel <pixel@mandriva.com> 0.6.5-1mdv2007.1
+ Revision: 133552
- new release
- drop menu (partimage is useful only as superuser)
- drop patch 2,4,5 (applied upstream)
- adapt patch 1,8
- updated %%doc
  (thanks to Olivier Lahaye)
- Import partimage

* Mon Nov 14 2005 Oden Eriksson <oeriksson@mandriva.com> 0.6.4-11mdk
- rebuilt against openssl-0.9.8a

* Fri Oct 21 2005 Pixel <pixel@mandriva.com> 0.6.4-10mdk
- dont discard some more error messages in batch mode (patch7)

* Thu Oct 20 2005 Pixel <pixel@mandriva.com> 0.6.4-9mdk
- dont discard error message in batch mode (patch7)

* Tue Oct 18 2005 Pixel <pixel@mandriva.com> 0.6.4-8mdk
- replace save_all and rest_all with save_file and rest_file 
  (we now use a perl script around partimage instead of 
   doing everything inside partimage with sfdisk)

* Wed Aug 24 2005 Gwenole Beauchesne <gbeauchesne@mandriva.com> 0.6.4-7mdk
- varargs fixes

* Mon Feb 21 2005 Gwenole Beauchesne <gbeauchesne@mandrakesoft.com> 0.6.4-6mdk
- 64-bit & lib64 fixes

* Mon Jan 31 2005 Pixel <pixel@mandrakesoft.com> 0.6.4-5mdk
- ensure the patch save_all_and_rest_all_actions is in the srpm
- add a service partimaged when in jail
- don't hardwire the automake directory, take any mkinstalldirs
- remove rubbish in info dir

* Mon Jan 24 2005 Pixel <pixel@mandrakesoft.com> 0.6.4-4mdk
- allow building with no authentication but in a jail
- in this forked version, add action save_all and rest_all

* Mon Nov 22 2004 Stefan van der Eijk <stefan@mandrake.org> 0.6.4-3mdk
- BuildRequires

* Sat Jul 24 2004 Marcel Pol <mpol@mandrake.org> 0.6.4-2mdk
- build against new slang

* Thu Jun 17 2004 Per Øyvind Karlsen <peroyvind@linux-mandrake.com> 0.6.4-1mdk
- 0.8.4
- cleanups
