Summary:	Utility for use with gnuddrescue to aid with data recovery
Name:		ddrutility
Version:	2.7
Release:	2.1
URL:		http://sourceforge.net/projects/ddrutility/
License:	GPL
Group:		Applications/Forensics Tools
Source:		%{name}-%{version}.tar.gz
Requires:	ntfsprogs
Requires:	util-linux
Requires:	sleuthkit
Requires:	e2fsprogs
Requires:	ddrescue

%description
Ddrutility is meant to be a compliment to gnuddrescue. It is a set of
utilities to help with hard drive data rescue. It currently contains
the following utilities:
	ddru_findbad
	ddru_ntfsbitmap
	ddru_ntfsfindbad (NEW)

Please see the Wiki (http://sourceforge.net/p/ddrutility/wiki/Home/) or
the help files for full documentation (note that the Wiki page does not
seem to navigate properly, sorry). The readme file contains the latest
news of updates, and can be viewed as text on the Files page.

%prep
%setup -q

%build
export LDFLAGS=-Wl,--allow-multiple-definition
%configure
make

%install
%makeinstall
rm -f %{buildroot}/%{_infodir}/dir

%clean
%{__rm} -rf %{buildroot}

%files
%doc AUTHORS ChangeLog COPYING README THANKS
%{_bindir}/%{name}
%{_bindir}/ddru_findbad
%{_bindir}/ddru_ntfsbitmap
%{_bindir}/ddru_ntfsfindbad
%{_bindir}/ddru_diskutility
%{_mandir}/man1/%{name}.1.*
%{_mandir}/man1/ddru_findbad.1.*
%{_mandir}/man1/ddru_ntfsbitmap.1.*
%{_mandir}/man1/ddru_ntfsfindbad.1.*
%{_mandir}/man1/ddru_diskutility.1.*
%{_infodir}/%{name}.info.*

%changelog
* Wed May 20 2015 Wei-Lun Chao <bluebat@member.fsf.org> - 2.7
- Rebuild for Fedora
* Sun Jan 11 2015 Lawrence R. Rogers <lrr@cert.org> 2.7-1
* Release 2.7-1
  * Ddru_ntfsfindbad 1.5 released:
    + Fixed possible program crash if partition boot sector error
    + Better partition boot sector error output
  * Ddru_ntfsbitmap 1.5 released:
    + Fixed possible program crash if partition boot sector error
    + Better partition boot sector error output
* Sat Jan 10 2015 Lawrence R. Rogers <lrr@cert.org> 2.6-4
	This really took place on January 22, 2015
	ntfscluster is in /bin on CentOS 6 only.
* Tue Nov 25 2014 Lawrence R. Rogers <lrr@cert.org> 2.6-3
	ntfscluster moved again in CentOS 6.
* Sat Nov 15 2014 Lawrence R. Rogers <lrr@cert.org> 2.6-2
	ntfscluster moved in CentOS 6.
* Wed Oct 15 2014 Lawrence R. Rogers <lrr@cert.org> 2.6-1
  * Changes have been made for compiling compatibility:
    + Some unneeded items removed from configure.ac
    + Added lib check for iconv
  * Some improvements have been made to the documentation:
    + Added examples to the --mftdomain option of ntfs_bitmap
    + Updated info about ddru_findbad being slow
  * Ddru_findbad 1.11 released:
    + No longer relies on bash
    + Fixed a bug dealing with bad ntfscluster results
    + Images are now accessed as read only
  * Ddru_ntfsfindbad 1.4 released:
    + Fixed potential memory bug with name conversions
    + Fixed iconv BOM issue
    + Fixed a bug with mft data run length
    + Fixed issue with current postition in logfile
  * Ddru_ntfsbitmap 1.4 released:
    + Fixed potential memory bug with name conversions
    + Fixed iconv BOM issue
  * Ddru_diskutility 1.3 released:
    + Initial release
* Sun Jun 08 2014 Lawrence R. Rogers <lrr@cert.org> 2.5-1
        Changes in version 2.5
		Some of the code has been restructured to allow for sharing of functions.
		Ddru_ntfsbitmap & ddru_ntfsfindbad - Both are now able to properly process non 512 byte sectors. They both can also now handle partial MFT errors,
		 meaning if the second sector of the record is bad and the record size fits in the first sector it will now process it instead of totally rejecting it.
		Ddru_ntfsbitmap - Fixed a bug where the MFT domain output file would end up with an error (same error that was fixed in domain output file previously).
		Ddru_ntfsbitmap & ddru_findbad - Both are now able to process the older NTFS filesystem from Windows NT and 2000.
	Changes in version 2.4 (released May 15 2014)
		Ddru_ntfsbitmap - Added option --restart to delete all important files from the previous run before starting. This is used to help prevent any issues from old
		 files causing bad results.
		Ddru_ntfsbitmap - Fixed a bug where the domain output file would end up with an error when using the --inputoffset option and the partition start position was
		 equal or less than what was considered the "first track" (63 sectors).
		Ddru_ntfsfindbad - Fixed a bug where files were falsely reported as having errors if the start or finish was right next to an error sector.
		 They would be listed but with a 0 byte error size.
		Ddru_ntfsfindbad - Fixed a bug in the debug output where the offset and full offset were not correct.
	Changes in version 2.3
		Ddru_ntfsfindbad - Fixed a bug where some file or folder names were in DOS 8.3 instead of Win32 format in the output.
		Ddru_ntfsfindbad now properly converts NTFS file names from UTF-16 to UTF-8, as opposed to just processing every other byte. This should allow for multi-language
		 support in the output. Added the option "--encoding" to be able to choose the filename output encoding, if needed to be different from the default of UTF-8.
		Ddru_ntfsfindbad - Added option --noconvert to turn off the new encoding option. This has been added in case of strange program crashes caused by the very buggy iconv.
	 	 When used, this option uses the old method of every other character for the file names, which will work for ASCII.
* Mon Mar 17 2014 Lawrence R. Rogers <lrr@cert.org> 2.2-1
        Initial version
