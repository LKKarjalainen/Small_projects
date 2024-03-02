# Short-hand names created using the following javascript:
# originalName.match(/^.|[A-Zlp\d]|[fuiv]*$/g).join('')
# Use directly as a sed script.
# If the exporter works, this won't change names that would clash.
s/gl\.canvas(/gl.c(/g
s/gl\.drawingBufferWidth(/gl.dBW(/g
s/gl\.drawingBufferHeight(/gl.dBH(/g
s/gl\.drawingBufferColorSpace(/gl.dBClSp(/g
s/gl\.unpackColorSpace(/gl.upClSp(/g
s/gl\.activeTexture(/gl.aT(/g
s/gl\.attachShader(/gl.aS(/g
s/gl\.beginQuery(/gl.bQ(/g
s/gl\.bindAttribLocation(/gl.bAL(/g
s/gl\.bindBufferBase(/gl.bBB(/g
s/gl\.bindBufferRange(/gl.bBR(/g
s/gl\.bindRenderbuffer(/gl.bR(/g
s/gl\.bindSampler(/gl.bSpl(/g
s/gl\.bindVertexArray(/gl.bVA(/g
s/gl\.blendColor(/gl.blCl(/g
s/gl\.blendEquation(/gl.blE(/g
s/gl\.blendEquationSeparate(/gl.blESp(/g
s/gl\.blendFuncSeparate(/gl.blFSp(/g
s/gl\.bufferData(/gl.bD(/g
s/gl\.bufferSubData(/gl.bSD(/g
s/gl\.checkFramebufferStatus(/gl.cFS(/g
s/gl\.clientWaitSync(/gl.clWS(/g
s/gl\.compileShader(/gl.cplS(/g
s/gl\.compressedTexImage3D(/gl.cpTI3D(/g
s/gl\.copyBufferSubData(/gl.cpBSD(/g
s/gl\.createBuffer(/gl.cB(/g
s/gl\.createFramebuffer(/gl.cF(/g
s/gl\.createProgram(/gl.cP(/g
s/gl\.createQuery(/gl.cQ(/g
s/gl\.createRenderbuffer(/gl.cR(/g
s/gl\.createSampler(/gl.cSpl(/g
s/gl\.createShader(/gl.cS(/g
s/gl\.createTexture(/gl.cT(/g
s/gl\.createTransformFeedback(/gl.cTF(/g
s/gl\.createVertexArray(/gl.cVA(/g
s/gl\.cullFace(/gl.cllF(/g
s/gl\.deleteBuffer(/gl.dlB(/g
s/gl\.deleteFramebuffer(/gl.dlF(/g
s/gl\.deleteProgram(/gl.dlP(/g
s/gl\.deleteQuery(/gl.dlQ(/g
s/gl\.deleteRenderbuffer(/gl.dlR(/g
s/gl\.deleteSampler(/gl.dlSpl(/g
s/gl\.deleteTexture(/gl.dlT(/g
s/gl\.deleteTransformFeedback(/gl.dlTF(/g
s/gl\.deleteVertexArray(/gl.dlVA(/g
s/gl\.depthFunc(/gl.dpF(/g
s/gl\.depthMask(/gl.dpM(/g
s/gl\.depthRange(/gl.dpR(/g
s/gl\.detachShader(/gl.dS(/g
s/gl\.disable(/gl.dl(/g
s/gl\.drawArraysInstanced(/gl.dAI(/g
s/gl\.drawElementsInstanced(/gl.dElI(/g
s/gl\.drawRangeElements(/gl.dREl(/g
s/gl\.enable(/gl.el(/g
s/gl\.endQuery(/gl.eQ(/g
s/gl\.endTransformFeedback(/gl.eTF(/g
s/gl\.fenceSync(/gl.fS(/g
s/gl\.finish(/gl.f(/g
s/gl\.flush(/gl.fl(/g
s/gl\.framebufferRenderbuffer(/gl.fR(/g
s/gl\.framebufferTexture2D(/gl.fT2D(/g
s/gl\.framebufferTextureLayer(/gl.fTL(/g
s/gl\.frontFace(/gl.fF(/g
s/gl\.generateMipmap(/gl.gMpp(/g
s/gl\.getActiveAttrib(/gl.gAA(/g
s/gl\.getActiveUniformBlockName(/gl.gAUBlN(/g
s/gl\.getActiveUniformBlockParameter(/gl.gAUBlP(/g
s/gl\.getAttachedShaders(/gl.gAS(/g
s/gl\.getAttribLocation(/gl.gAL(/g
s/gl\.getBufferParameter(/gl.gBP(/g
s/gl\.getBufferSubData(/gl.gBSD(/g
s/gl\.getContextAttributes(/gl.gCA(/g
s/gl\.getFragDataLocation(/gl.gFDL(/g
s/gl\.getFramebufferAttachmentParameter(/gl.gFAP(/g
s/gl\.getIndexedParameter(/gl.gIP(/g
s/gl\.getInternalformatParameter(/gl.gIlP(/g
s/gl\.getParameter(/gl.gP(/g
s/gl\.getProgramInfoLog(/gl.gPIL(/g
s/gl\.getProgramParameter(/gl.gPP(/g
s/gl\.getQuery(/gl.gQ(/g
s/gl\.getQueryParameter(/gl.gQP(/g
s/gl\.getRenderbufferParameter(/gl.gRP(/g
s/gl\.getSamplerParameter(/gl.gSplP(/g
s/gl\.getShaderInfoLog(/gl.gSIL(/g
s/gl\.getShaderPrecisionFormat(/gl.gSPF(/g
s/gl\.getShaderSource(/gl.gSS(/g
s/gl\.getSupportedExtensions(/gl.gSppE(/g
s/gl\.getTexParameter(/gl.gTP(/g
s/gl\.getTransformFeedbackVarying(/gl.gTFV(/g
s/gl\.getUniform(/gl.gU(/g
s/gl\.getUniformBlockIndex(/gl.gUBlI(/g
s/gl\.getUniformIndices(/gl.gUI(/g
s/gl\.getUniformLocation(/gl.gUL(/g
s/gl\.getVertexAttrib(/gl.gVA(/g
s/gl\.getVertexAttribOffset(/gl.gVAO(/g
s/gl\.hint(/gl.h(/g
s/gl\.invalidateFramebuffer(/gl.ilF(/g
s/gl\.invalidateSubFramebuffer(/gl.ilSF(/g
s/gl\.isBuffer(/gl.iB(/g
s/gl\.isContextLost(/gl.iCL(/g
s/gl\.isEnabled(/gl.iEl(/g
s/gl\.isFramebuffer(/gl.iF(/g
s/gl\.isProgram(/gl.iP(/g
s/gl\.isQuery(/gl.iQ(/g
s/gl\.isRenderbuffer(/gl.iR(/g
s/gl\.isSampler(/gl.iSpl(/g
s/gl\.isTexture(/gl.iT(/g
s/gl\.isTransformFeedback(/gl.iTF(/g
s/gl\.isVertexArray(/gl.iVA(/g
s/gl\.lineWidth(/gl.lW(/g
s/gl\.linkProgram(/gl.lP(/g
s/gl\.pauseTransformFeedback(/gl.pTF(/g
s/gl\.pixelStorei(/gl.plSi(/g
s/gl\.polygonOffset(/gl.plO(/g
s/gl\.readBuffer(/gl.rB(/g
s/gl\.readPixels(/gl.rPl(/g
s/gl\.renderbufferStorage(/gl.rS(/g
s/gl\.renderbufferStorageMultisample(/gl.rSMlpl(/g
s/gl\.resumeTransformFeedback(/gl.rTF(/g
s/gl\.sampleCoverage(/gl.splC(/g
s/gl\.samplerParameterf(/gl.splPf(/g
s/gl\.samplerParameteri(/gl.splPi(/g
s/gl\.shaderSource(/gl.sS(/g
s/gl\.stencilFunc(/gl.slF(/g
s/gl\.stencilFuncSeparate(/gl.slFSp(/g
s/gl\.stencilMask(/gl.slM(/g
s/gl\.stencilMaskSeparate(/gl.slMSp(/g
s/gl\.stencilOp(/gl.slOp(/g
s/gl\.stencilOpSeparate(/gl.slOpSp(/g
s/gl\.texImage2D(/gl.tI2D(/g
s/gl\.texImage3D(/gl.tI3D(/g
s/gl\.texParameterf(/gl.tPf(/g
s/gl\.texParameteri(/gl.tPi(/g
s/gl\.texStorage2D(/gl.tS2D(/g
s/gl\.texStorage3D(/gl.tS3D(/g
s/gl\.texSubImage2D(/gl.tSI2D(/g
s/gl\.texSubImage3D(/gl.tSI3D(/g
s/gl\.transformFeedbackVaryings(/gl.tFV(/g
s/gl\.uniform1ui(/gl.u1ui(/g
s/gl\.uniform2ui(/gl.u2ui(/g
s/gl\.uniform3ui(/gl.u3ui(/g
s/gl\.uniform4ui(/gl.u4ui(/g
s/gl\.uniformBlockBinding(/gl.uBlB(/g
s/gl\.useProgram(/gl.uP(/g
s/gl\.validateProgram(/gl.vlP(/g
s/gl\.vertexAttribDivisor(/gl.vAD(/g
s/gl\.vertexAttribI4i(/gl.vAI4i(/g
s/gl\.vertexAttribI4ui(/gl.vAI4ui(/g
s/gl\.vertexAttribIPointer(/gl.vAIP(/g
s/gl\.waitSync(/gl.wS(/g
s/gl\.bindBuffer(/gl.bB(/g
s/gl\.bindFramebuffer(/gl.bF(/g
s/gl\.bindTexture(/gl.bT(/g
s/gl\.clear(/gl.cl(/g
s/gl\.clearBufferfi(/gl.clBfi(/g
s/gl\.clearBufferfv(/gl.clBfv(/g
s/gl\.clearBufferiv(/gl.clBiv(/g
s/gl\.clearBufferuiv(/gl.clBuiv(/g
s/gl\.clearColor(/gl.clCl(/g
s/gl\.clearDepth(/gl.clDp(/g
s/gl\.clearStencil(/gl.clSl(/g
s/gl\.colorMask(/gl.clM(/g
s/gl\.disableVertexAttribArray(/gl.dlVAA(/g
s/gl\.drawArrays(/gl.dA(/g
s/gl\.drawBuffers(/gl.dB(/g
s/gl\.drawElements(/gl.dEl(/g
s/gl\.enableVertexAttribArray(/gl.elVAA(/g
s/gl\.scissor(/gl.s(/g
s/gl\.uniform1f(/gl.u1f(/g
s/gl\.uniform1fv(/gl.u1fv(/g
s/gl\.uniform1i(/gl.u1i(/g
s/gl\.uniform1iv(/gl.u1iv(/g
s/gl\.uniform1uiv(/gl.u1uiv(/g
s/gl\.uniform2f(/gl.u2f(/g
s/gl\.uniform2fv(/gl.u2fv(/g
s/gl\.uniform2i(/gl.u2i(/g
s/gl\.uniform2iv(/gl.u2iv(/g
s/gl\.uniform2uiv(/gl.u2uiv(/g
s/gl\.uniform3f(/gl.u3f(/g
s/gl\.uniform3fv(/gl.u3fv(/g
s/gl\.uniform3i(/gl.u3i(/g
s/gl\.uniform3iv(/gl.u3iv(/g
s/gl\.uniform3uiv(/gl.u3uiv(/g
s/gl\.uniform4f(/gl.u4f(/g
s/gl\.uniform4fv(/gl.u4fv(/g
s/gl\.uniform4i(/gl.u4i(/g
s/gl\.uniform4iv(/gl.u4iv(/g
s/gl\.uniform4uiv(/gl.u4uiv(/g
s/gl\.uniformMatrix2fv(/gl.uM2fv(/g
s/gl\.uniformMatrix2x3fv(/gl.uM23fv(/g
s/gl\.uniformMatrix2x4fv(/gl.uM24fv(/g
s/gl\.uniformMatrix3fv(/gl.uM3fv(/g
s/gl\.uniformMatrix3x2fv(/gl.uM32fv(/g
s/gl\.uniformMatrix3x4fv(/gl.uM34fv(/g
s/gl\.uniformMatrix4fv(/gl.uM4fv(/g
s/gl\.uniformMatrix4x2fv(/gl.uM42fv(/g
s/gl\.uniformMatrix4x3fv(/gl.uM43fv(/g
s/gl\.vertexAttrib1f(/gl.vA1f(/g
s/gl\.vertexAttrib1fv(/gl.vA1fv(/g
s/gl\.vertexAttrib2f(/gl.vA2f(/g
s/gl\.vertexAttrib2fv(/gl.vA2fv(/g
s/gl\.vertexAttrib3f(/gl.vA3f(/g
s/gl\.vertexAttrib3fv(/gl.vA3fv(/g
s/gl\.vertexAttrib4f(/gl.vA4f(/g
s/gl\.vertexAttrib4fv(/gl.vA4fv(/g
s/gl\.vertexAttribI4iv(/gl.vAI4iv(/g
s/gl\.vertexAttribI4uiv(/gl.vAI4uiv(/g
s/gl\.vertexAttribPointer(/gl.vAP(/g
s/gl\.viewport(/gl.vp(/g
s/gl\.makeXRCompatible(/gl.mXRCpl(/g