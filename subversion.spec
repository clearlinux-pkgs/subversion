#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : subversion
Version  : 1.10.0
Release  : 5
URL      : http://mirror.cc.columbia.edu/pub/software/apache/subversion/subversion-1.10.0.tar.bz2
Source0  : http://mirror.cc.columbia.edu/pub/software/apache/subversion/subversion-1.10.0.tar.bz2
Summary  : Subversion Delta Library
Group    : Development/Tools
License  : Apache-2.0 BSD-2-Clause BSD-3-Clause MIT
Requires: subversion-bin
Requires: subversion-lib
Requires: subversion-locales
Requires: subversion-doc
BuildRequires : apr-dev
BuildRequires : apr-util-dev
BuildRequires : dbus-dev
BuildRequires : doxygen
BuildRequires : expat-dev
BuildRequires : pbr
BuildRequires : pip
BuildRequires : pkgconfig(liblz4)
BuildRequires : pkgconfig(serf-1)
BuildRequires : pkgconfig(zlib)
BuildRequires : python-dev
BuildRequires : python3-dev
BuildRequires : ruby
BuildRequires : sed
BuildRequires : setuptools
BuildRequires : sqlite-autoconf-dev
Patch1: CVE-2017-9800.nopatch

%description
Subversion, a version control system.
=====================================
$LastChangedDate: 2016-05-31 14:07:51 +0000 (Tue, 31 May 2016) $

%package bin
Summary: bin components for the subversion package.
Group: Binaries

%description bin
bin components for the subversion package.


%package dev
Summary: dev components for the subversion package.
Group: Development
Requires: subversion-lib
Requires: subversion-bin
Provides: subversion-devel

%description dev
dev components for the subversion package.


%package doc
Summary: doc components for the subversion package.
Group: Documentation

%description doc
doc components for the subversion package.


%package lib
Summary: lib components for the subversion package.
Group: Libraries

%description lib
lib components for the subversion package.


%package locales
Summary: locales components for the subversion package.
Group: Default

%description locales
locales components for the subversion package.


%prep
%setup -q -n subversion-1.10.0

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1526023858
export CFLAGS="$CFLAGS -fstack-protector-strong -mzero-caller-saved-regs=used "
export FCFLAGS="$CFLAGS -fstack-protector-strong -mzero-caller-saved-regs=used "
export FFLAGS="$CFLAGS -fstack-protector-strong -mzero-caller-saved-regs=used "
export CXXFLAGS="$CXXFLAGS -fstack-protector-strong -mzero-caller-saved-regs=used "
%configure --disable-static --with-utf8proc=internal \
--without-swig \
--with-serf
make  %{?_smp_mflags}

%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make VERBOSE=1 V=1 %{?_smp_mflags} check

%install
export SOURCE_DATE_EPOCH=1526023858
rm -rf %{buildroot}
%make_install
%find_lang subversion

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/svn
/usr/bin/svnadmin
/usr/bin/svnbench
/usr/bin/svndumpfilter
/usr/bin/svnfsfs
/usr/bin/svnlook
/usr/bin/svnmucc
/usr/bin/svnrdump
/usr/bin/svnserve
/usr/bin/svnsync
/usr/bin/svnversion

%files dev
%defattr(-,root,root,-)
/usr/include/subversion-1/mod_authz_svn.h
/usr/include/subversion-1/mod_dav_svn.h
/usr/include/subversion-1/svn-revision.txt
/usr/include/subversion-1/svn_auth.h
/usr/include/subversion-1/svn_base64.h
/usr/include/subversion-1/svn_cache_config.h
/usr/include/subversion-1/svn_checksum.h
/usr/include/subversion-1/svn_client.h
/usr/include/subversion-1/svn_cmdline.h
/usr/include/subversion-1/svn_compat.h
/usr/include/subversion-1/svn_config.h
/usr/include/subversion-1/svn_ctype.h
/usr/include/subversion-1/svn_dav.h
/usr/include/subversion-1/svn_delta.h
/usr/include/subversion-1/svn_diff.h
/usr/include/subversion-1/svn_dirent_uri.h
/usr/include/subversion-1/svn_dso.h
/usr/include/subversion-1/svn_error.h
/usr/include/subversion-1/svn_error_codes.h
/usr/include/subversion-1/svn_fs.h
/usr/include/subversion-1/svn_hash.h
/usr/include/subversion-1/svn_io.h
/usr/include/subversion-1/svn_iter.h
/usr/include/subversion-1/svn_md5.h
/usr/include/subversion-1/svn_mergeinfo.h
/usr/include/subversion-1/svn_nls.h
/usr/include/subversion-1/svn_opt.h
/usr/include/subversion-1/svn_path.h
/usr/include/subversion-1/svn_pools.h
/usr/include/subversion-1/svn_props.h
/usr/include/subversion-1/svn_quoprint.h
/usr/include/subversion-1/svn_ra.h
/usr/include/subversion-1/svn_ra_svn.h
/usr/include/subversion-1/svn_repos.h
/usr/include/subversion-1/svn_sorts.h
/usr/include/subversion-1/svn_string.h
/usr/include/subversion-1/svn_subst.h
/usr/include/subversion-1/svn_time.h
/usr/include/subversion-1/svn_types.h
/usr/include/subversion-1/svn_user.h
/usr/include/subversion-1/svn_utf.h
/usr/include/subversion-1/svn_version.h
/usr/include/subversion-1/svn_wc.h
/usr/include/subversion-1/svn_x509.h
/usr/include/subversion-1/svn_xml.h
/usr/lib64/libsvn_client-1.so
/usr/lib64/libsvn_delta-1.so
/usr/lib64/libsvn_diff-1.so
/usr/lib64/libsvn_fs-1.so
/usr/lib64/libsvn_fs_fs-1.so
/usr/lib64/libsvn_fs_util-1.so
/usr/lib64/libsvn_fs_x-1.so
/usr/lib64/libsvn_ra-1.so
/usr/lib64/libsvn_ra_local-1.so
/usr/lib64/libsvn_ra_serf-1.so
/usr/lib64/libsvn_ra_svn-1.so
/usr/lib64/libsvn_repos-1.so
/usr/lib64/libsvn_subr-1.so
/usr/lib64/libsvn_wc-1.so
/usr/lib64/pkgconfig/libsvn_client.pc
/usr/lib64/pkgconfig/libsvn_delta.pc
/usr/lib64/pkgconfig/libsvn_diff.pc
/usr/lib64/pkgconfig/libsvn_fs.pc
/usr/lib64/pkgconfig/libsvn_fs_fs.pc
/usr/lib64/pkgconfig/libsvn_fs_util.pc
/usr/lib64/pkgconfig/libsvn_fs_x.pc
/usr/lib64/pkgconfig/libsvn_ra.pc
/usr/lib64/pkgconfig/libsvn_ra_local.pc
/usr/lib64/pkgconfig/libsvn_ra_serf.pc
/usr/lib64/pkgconfig/libsvn_ra_svn.pc
/usr/lib64/pkgconfig/libsvn_repos.pc
/usr/lib64/pkgconfig/libsvn_subr.pc
/usr/lib64/pkgconfig/libsvn_wc.pc

%files doc
%defattr(-,root,root,-)
%doc /usr/share/man/man1/*
%doc /usr/share/man/man5/*
%doc /usr/share/man/man8/*

%files lib
%defattr(-,root,root,-)
/usr/lib64/libsvn_client-1.so.0
/usr/lib64/libsvn_client-1.so.0.0.0
/usr/lib64/libsvn_delta-1.so.0
/usr/lib64/libsvn_delta-1.so.0.0.0
/usr/lib64/libsvn_diff-1.so.0
/usr/lib64/libsvn_diff-1.so.0.0.0
/usr/lib64/libsvn_fs-1.so.0
/usr/lib64/libsvn_fs-1.so.0.0.0
/usr/lib64/libsvn_fs_fs-1.so.0
/usr/lib64/libsvn_fs_fs-1.so.0.0.0
/usr/lib64/libsvn_fs_util-1.so.0
/usr/lib64/libsvn_fs_util-1.so.0.0.0
/usr/lib64/libsvn_fs_x-1.so.0
/usr/lib64/libsvn_fs_x-1.so.0.0.0
/usr/lib64/libsvn_ra-1.so.0
/usr/lib64/libsvn_ra-1.so.0.0.0
/usr/lib64/libsvn_ra_local-1.so.0
/usr/lib64/libsvn_ra_local-1.so.0.0.0
/usr/lib64/libsvn_ra_serf-1.so.0
/usr/lib64/libsvn_ra_serf-1.so.0.0.0
/usr/lib64/libsvn_ra_svn-1.so.0
/usr/lib64/libsvn_ra_svn-1.so.0.0.0
/usr/lib64/libsvn_repos-1.so.0
/usr/lib64/libsvn_repos-1.so.0.0.0
/usr/lib64/libsvn_subr-1.so.0
/usr/lib64/libsvn_subr-1.so.0.0.0
/usr/lib64/libsvn_wc-1.so.0
/usr/lib64/libsvn_wc-1.so.0.0.0

%files locales -f subversion.lang
%defattr(-,root,root,-)

