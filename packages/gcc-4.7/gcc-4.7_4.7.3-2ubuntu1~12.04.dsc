-----BEGIN PGP SIGNED MESSAGE-----
Hash: SHA1

Format: 1.0
Source: gcc-4.7
Binary: gcc-4.7-base, libgcc-4.7-dev, lib64gcc-4.7-dev, lib32gcc-4.7-dev, libhfgcc-4.7-dev, libsfgcc-4.7-dev, libn32gcc-4.7-dev, gcc-4.7, gcc-4.7-multilib, gcc-4.7-plugin-dev, gcc-4.7-hppa64, gcc-4.7-spu, g++-4.7-spu, gfortran-4.7-spu, cpp-4.7, cpp-4.7-doc, gcc-4.7-locales, g++-4.7, g++-4.7-multilib, libmudflap0-4.7-dev, gobjc++-4.7, gobjc++-4.7-multilib, gobjc-4.7, gobjc-4.7-multilib, libobjc-4.7-dev, lib64objc-4.7-dev, lib32objc-4.7-dev, libn32objc-4.7-dev, libhfobjc-4.7-dev, libsfobjc-4.7-dev, gfortran-4.7, gfortran-4.7-multilib, gfortran-4.7-doc, libgfortran-4.7-dev, lib64gfortran-4.7-dev, lib32gfortran-4.7-dev, libn32gfortran-4.7-dev, libhfgfortran-4.7-dev, libsfgfortran-4.7-dev, gccgo-4.7, gccgo-4.7-multilib, gccgo-4.7-doc, libgo0, libgo0-dbg, lib64go0, lib64go0-dbg, lib32go0, lib32go0-dbg, libn32go0, libn32go0-dbg, libstdc++6-4.7-dev, libstdc++6-4.7-pic, libstdc++6-4.7-dbg, lib32stdc++6-4.7-dev, lib32stdc++6-4.7-dbg, lib64stdc++6-4.7-dev, lib64stdc++6-4.7-dbg,
 libn32stdc++6-4.7-dev, libn32stdc++6-4.7-dbg, libhfstdc++6-4.7-dev, libhfstdc++6-4.7-dbg, libsfstdc++6-4.7-dev, libsfstdc++6-4.7-dbg, libstdc++6-4.7-doc, gcc-4.7-soft-float, gcc-4.7-doc,
 gcc-4.7-source
Architecture: any all
Version: 4.7.3-2ubuntu1~12.04
Maintainer: Ubuntu Core developers <ubuntu-devel-discuss@lists.ubuntu.com>
Uploaders: Matthias Klose <doko@debian.org>
Homepage: http://gcc.gnu.org/
Standards-Version: 3.9.3
Vcs-Browser: http://svn.debian.org/viewsvn/gcccvs/branches/sid/gcc-4.7/
Vcs-Svn: svn://svn.debian.org/svn/gcccvs/branches/sid/gcc-4.7
Build-Depends: debhelper (>= 5.0.62), libc6.1-dev (>= 2.13-0ubuntu6) [alpha ia64] | libc0.3-dev (>= 2.13-0ubuntu6) [hurd-i386] | libc0.1-dev (>= 2.13-0ubuntu6) [kfreebsd-i386 kfreebsd-amd64] | libc6-dev (>= 2.13-0ubuntu6), libc6-dev (>= 2.13-31) [armel armhf], libc6-dev-amd64 [i386 x32], libc6-dev-sparc64 [sparc], libc6-dev-s390 [s390x], libc6-dev-s390x [s390], libc6-dev-i386 [amd64 x32], libc6-dev-powerpc [ppc64], libc6-dev-ppc64 [powerpc], libc0.1-dev-i386 [kfreebsd-amd64], lib32gcc1 [amd64 ppc64 kfreebsd-amd64 s390x x32], lib64gcc1 [i386 powerpc sparc s390 x32], libc6-dev-mips64 [mips mipsel], libc6-dev-mipsn32 [mips mipsel], libc6-dev-armhf [armel], libc6-dev-armel [armhf], m4, libtool, autoconf2.64, automake (>= 1:1.11), automake (<< 1:1.12), libunwind7-dev (>= 0.98.5-6) [ia64], libatomic-ops-dev [ia64], zlib1g-dev, gawk, lzma, xz-utils, patchutils, binutils-hppa64 (>= 2.22) [hppa], gperf (>= 3.0.1), bison (>= 1:2.3), flex, gettext, texinfo (>= 4.3), locales, sharutils, procps, netbase, binutils-spu (>= 2.22) [powerpc ppc64], newlib-spu (>= 1.16.0) [powerpc ppc64], libcloog-ppl-dev (>= 0.15.11), libmpc-dev, libmpfr-dev (>= 3.0.0-9~), libgmp-dev (>= 2:5.0.1~), dejagnu [!m68k !arm !armel !armhf !hurd-i386 !hurd-alpha], autogen, realpath (>= 1.9.12), chrpath, lsb-release, quilt
Build-Depends-Indep: doxygen (>= 1.7.2), graphviz (>= 2.2), ghostscript, texlive-latex-base, xsltproc, libxml2-utils, docbook-xsl-ns
Build-Conflicts: binutils-gold
Package-List: 
 cpp-4.7 deb interpreters optional
 cpp-4.7-doc deb doc optional
 g++-4.7 deb devel optional
 g++-4.7-multilib deb devel optional
 g++-4.7-spu deb devel optional
 gcc-4.7 deb devel optional
 gcc-4.7-base deb libs required
 gcc-4.7-doc deb doc optional
 gcc-4.7-hppa64 deb devel optional
 gcc-4.7-locales deb devel optional
 gcc-4.7-multilib deb devel optional
 gcc-4.7-plugin-dev deb devel optional
 gcc-4.7-soft-float deb devel optional
 gcc-4.7-source deb devel optional
 gcc-4.7-spu deb devel optional
 gccgo-4.7 deb devel optional
 gccgo-4.7-doc deb doc optional
 gccgo-4.7-multilib deb devel optional
 gfortran-4.7 deb devel optional
 gfortran-4.7-doc deb doc optional
 gfortran-4.7-multilib deb devel optional
 gfortran-4.7-spu deb devel optional
 gobjc++-4.7 deb devel optional
 gobjc++-4.7-multilib deb devel optional
 gobjc-4.7 deb devel optional
 gobjc-4.7-multilib deb devel optional
 lib32gcc-4.7-dev deb libdevel optional
 lib32gfortran-4.7-dev deb libdevel optional
 lib32go0 deb libs optional
 lib32go0-dbg deb debug extra
 lib32objc-4.7-dev deb libdevel optional
 lib32stdc++6-4.7-dbg deb debug extra
 lib32stdc++6-4.7-dev deb libdevel optional
 lib64gcc-4.7-dev deb libdevel optional
 lib64gfortran-4.7-dev deb libdevel optional
 lib64go0 deb libs optional
 lib64go0-dbg deb debug extra
 lib64objc-4.7-dev deb libdevel optional
 lib64stdc++6-4.7-dbg deb debug extra
 lib64stdc++6-4.7-dev deb libdevel optional
 libgcc-4.7-dev deb libdevel optional
 libgfortran-4.7-dev deb libdevel optional
 libgo0 deb libs optional
 libgo0-dbg deb debug extra
 libhfgcc-4.7-dev deb libdevel optional
 libhfgfortran-4.7-dev deb libdevel optional
 libhfobjc-4.7-dev deb libdevel optional
 libhfstdc++6-4.7-dbg deb debug extra
 libhfstdc++6-4.7-dev deb libdevel optional
 libmudflap0-4.7-dev deb libdevel optional
 libn32gcc-4.7-dev deb libdevel optional
 libn32gfortran-4.7-dev deb libdevel optional
 libn32go0 deb libs optional
 libn32go0-dbg deb debug extra
 libn32objc-4.7-dev deb libdevel optional
 libn32stdc++6-4.7-dbg deb debug extra
 libn32stdc++6-4.7-dev deb libdevel optional
 libobjc-4.7-dev deb libdevel optional
 libsfgcc-4.7-dev deb libdevel optional
 libsfgfortran-4.7-dev deb libdevel optional
 libsfobjc-4.7-dev deb libdevel optional
 libsfstdc++6-4.7-dbg deb debug extra
 libsfstdc++6-4.7-dev deb libdevel optional
 libstdc++6-4.7-dbg deb debug extra
 libstdc++6-4.7-dev deb libdevel optional
 libstdc++6-4.7-doc deb doc optional
 libstdc++6-4.7-pic deb libdevel extra
Checksums-Sha1: 
 8f0a6bfe9229d8e48907f7b0e8968e39b73e6fb9 65736124 gcc-4.7_4.7.3.orig.tar.gz
 22022e33162970a42f35551559bb7ca8309de505 1020935 gcc-4.7_4.7.3-2ubuntu1~12.04.diff.gz
Checksums-Sha256: 
 f5133e299c86a949348b83aaf21c5ddb0a79088bad51e9fb812a33d1fb6f04a4 65736124 gcc-4.7_4.7.3.orig.tar.gz
 e7f5f48738e543d860fa048e36225db7b2bd1ac2caff62d05a51c1ccef663ab8 1020935 gcc-4.7_4.7.3-2ubuntu1~12.04.diff.gz
Files: 
 007397bf9999481511b6bc8e32c4540d 65736124 gcc-4.7_4.7.3.orig.tar.gz
 648ecd7bce4bfefcce6b5ed7f83dcfad 1020935 gcc-4.7_4.7.3-2ubuntu1~12.04.diff.gz
Original-Maintainer: Debian GCC Maintainers <debian-gcc@lists.debian.org>

-----BEGIN PGP SIGNATURE-----
Version: GnuPG v1.4.12 (GNU/Linux)

iEYEARECAAYFAlF0KXIACgkQStlRaw+TLJwmQACgvkgiPLG+Phi/d6DDM5F1P0Tq
uGsAoJTqPIeB3duv5+jUkdSnWfI70Zzf
=yYPZ
-----END PGP SIGNATURE-----
